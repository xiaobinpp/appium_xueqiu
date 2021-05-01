# -*- coding: utf-8 -*-
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.article import Article
from page.base_page import BasePage
from page.mine import Mine
from page.usermain import UserMain


class Main(BasePage):

    def goto_mine(self):
        self.find(MobileBy.XPATH,
                  '//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[5]/android.widget.TextView').click()
        return Mine(self._driver)

    def goto_usermain(self):
        return UserMain()

    def goto_article(self):
        return Article()

    def goto_trade(self):

        self.find(MobileBy.XPATH,
                  '//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[4]/android.widget.TextView').click()

        return


    # def glike(self):
    #     return self
    #
    # def comment(self):
    #     return self
