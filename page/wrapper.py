# -*- coding: utf-8 -*-
import logging

import allure
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args,**kwargs):

        # info以上级别的日志都会被打印
        logging.basicConfig(level=logging.INFO)

        # 黑名单弹框，包含的text
        _blacklist = [
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="下次再说"]'),
            (By.XPATH, '//*[@text="同意"]'),
        ]
        # 循环时设置隐式等待时间用到
        _error_num = 0
        _max_num = 3

        #局部导入，防止循环调用导致的卡死
        from page.base_page import BasePage
        instance:BasePage = args[0]
        try:
            logging.info('run'+ func.__name__ + "args:" + str(args[1:]) + "kwargs:" + str(kwargs))
            #未找到元素，则判断异常，查找当前页面是否存在黑名单名称，若存在则认为是弹框，尝试将弹框点击
            #判断传入的是否是元祖，是元祖的话，则提取元祖元素进行传参
            element = func(*args, **kwargs)
            if element == []:
                raise Exception('finds未查找到元素')
            #如果查找到元素，则把变量设置为0，下次有元素再查找时初始值还是0；
            #如果查找到元素，则需要把隐式等待时间设置回去
            _error_num = 0
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            logging.error('查找元素异常，进入黑名单弹框异常处理')
            # 调用BP中定义的方法进行截图
            instance.screenshot('tmp.png')

            # 将截图添加到allure报告中,allure报告只能接收二进制，所以需要读取图片
            with open('./tmp.png','rb') as m:
                content = m.read()
            allure.attach(content,name='tmp.png',attachment_type=allure.attachment_type.PNG)

            #如果发现异常，则设置隐式等待的时间为1，便于快速的查找到黑名单弹框，进行点击
            #发现异常，循环3次后，还未查找到则抛出异常，3次的次数由黑名单弹框的长度决定
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num +=1
            for ele in _blacklist:
                #如果找到黑名单元素，则放到列表里，列表正常应该只有一个黑名单元素
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    #处理完弹框，再次查找元素
                    return wrapper(*args,**kwargs)
    return wrapper


