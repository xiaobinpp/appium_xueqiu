# -*- coding: utf-8 -*-
from page.base_page import BasePage
from page.openaccount import OpenAccount


class Trade(BasePage):

    def goto_openaccount(self):
        return OpenAccount(self._driver)
