# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Mine(BasePage):

    def goto_login(self):
        self.find(MobileBy.XPATH,"//*[@text='帐号密码登录']").click()
        from page.login import Login
        return Login(self._driver)


    def get_toast(self):
        gtoast = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        print(gtoast)
        return gtoast