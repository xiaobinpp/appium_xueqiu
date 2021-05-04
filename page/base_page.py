# -*- coding: utf-8 -*-
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
import logging

from selenium.webdriver.common.by import By

from page.wrapper import handle_black


class BasePage():

    _params = {}

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def set_implicitly(self,time):
        self._driver.implicitly_wait(time)


    #装饰器的方式处理异常黑名单弹框
    @handle_black
    def find(self,by,locator):
        ele:WebElement
        if isinstance(by, tuple):
            ele = self._driver.find_element(*by)
        else:
            ele = self._driver.find_element(by, locator)
        return ele


    @handle_black
    def finds(self,by,locator):
        eles:list
        if isinstance(by, tuple):
            eles = self._driver.find_elements(*by)
            print(f"eles:{eles}")
        else:
            eles = self._driver.find_elements(by, locator)
        return eles

    #普通方法实现异常弹框黑名单的处理，上面使用装饰器的方式
    # def find(self,by,locator):
    #     # 判断传入的是否是元祖，是元祖的话，则提取元祖元素进行传参
    #     try:
    #         #未找到元素，则判断异常，查找当前页面是否存在黑名单名称，若存在则认为是弹框，尝试将弹框点击
    #         #判断传入的是否是元祖，是元祖的话，则提取元祖元素进行传参
    #         element:WebElement
    #         if isinstance(by,tuple):
    #             element = self._driver.find_element(*by)
    #         else:
    #             element = self._driver.find_element(by,locator)
    #         #如果查找到元素，则把变量设置为0，下次有元素再查找时初始值还是0；
    #         #如果查找到元素，则需要把隐式等待时间设置回去
    #         self._error_num = 0
    #         self._driver.implicitly_wait(10)
    #         return element
    #     except Exception as e:
    #         #如果发现异常，则设置隐式等待的时间为1，便于快速的查找到黑名单弹框，进行点击
    #         #发现异常，循环3次后，还未查找到则抛出异常，3次的次数由黑名单弹框的长度决定
    #         self._driver.implicitly_wait(1)
    #         if self._error_num > self._max_num:
    #             raise e
    #         self._error_num +=1
    #
    #         for ele in self._blacklist:
    #             #如果找到黑名单元素，则放到列表里，列表正常应该只有一个黑名单元素
    #             elelist = self._driver.find_elements(*ele)
    #             if len(elelist) > 0:
    #                 elelist[0].click()
    #                 return self.find(by,locator)


    def steps(self,path):
        with open(path) as f:
            #取出由谁调用的该函数
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        element = None

        raws = json.dumps(steps)
        for key,value in self._params.items():
            raws = raws.replace(f"${{{key}}}",value)
        steps = json.loads(raws)

        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    self.find(step['by'],step['locator']).click()
                if action == 'send':
                    self.find(step['by'],step['locator']).send_keys(step['value'])
                if action == 'is':
                    eles = self.find(step['by'],step['locator'])
                    return eles

    def screenshot(self,path):
        self._driver.save_screenshot(path)








