# -*- coding: utf-8 -*-
from page.base_page import BasePage
from page.search import Search


class Market(BasePage):

    def goto_seacrh(self):
        return Search(self._driver)



