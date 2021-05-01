# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Login(BasePage):

    def input_account(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/login_account"]').send_keys('***')
        return self

    def input_passwd(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/login_password"][@text="请输入登录密码"]').send_keys('***')
        print('输入密码')
        return self

    def click_login(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/button_next"]').click()
        print('点击登录')
        from page.mine import Mine
        return Mine(self._driver)



