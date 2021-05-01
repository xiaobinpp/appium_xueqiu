# -*- coding: utf-8 -*-
import logging

import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    def start(self):
        #如果driver=None，则说明是首次打开app
        if self._driver == None:
            logging.info('driver=None，读取yaml配置文件')
            with open('../config/data.yaml','r',encoding='utf-8') as file:
                data = yaml.load(file)
            caps = {}
            caps['platformName'] = data['platformName']
            caps['deviceName'] = data['deviceName']
            caps['appPackage'] = data['appPackage']
            caps['appActivity'] = data['appActivity']
            # caps['noReset'] = data['noReset']
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        else:

            self._driver.launch_app()

        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def end(self):
        pass

    def goto_main(self) -> Main:
        return Main(self._driver)