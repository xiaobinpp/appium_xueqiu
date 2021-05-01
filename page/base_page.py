# -*- coding: utf-8 -*-
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
import logging

from selenium.webdriver.common.by import By


class BasePage():

    #黑名单弹框，包含的text
    _blacklist=[
        (By.XPATH, '//*[@text="确认"]'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.XPATH, '//*[@text="同意"]'),
    ]

    #循环时设置隐式等待时间用到
    _max_num = 3
    _error_num = 0

    def __init__(self,driver:WebDriver=None):
        self._driver = driver


    def find(self,by,locator):
        try:
            #未找到元素，则判断异常，查找当前页面是否存在黑名单名称，若存在则认为是弹框，尝试将弹框点击
            #判断传入的是否是元祖，是元祖的话，则提取元祖元素进行传参
            element:WebElement
            if isinstance(by,tuple):
                element = self._driver.find_element(*by)
            else:
                element = self._driver.find_element(by,locator)
            #如果查找到元素，则把变量设置为0，下次有元素再查找时初始值还是0；
            #如果查找到元素，则需要把隐式等待时间设置回去
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            #如果发现异常，则设置隐式等待的时间为1，便于快速的查找到黑名单弹框，进行点击
            #发现异常，循环3次后，还未查找到则抛出异常，3次的次数由黑名单弹框的长度决定
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num +=1

            for ele in self._blacklist:
                #如果找到黑名单元素，则放到列表里，列表正常应该只有一个黑名单元素
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find(by,locator)









