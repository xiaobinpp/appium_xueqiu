# -*- coding: utf-8 -*-
from page.base_page import BasePage


class Search(BasePage):

    def search(self,name):
        self._params["name"] = name
        self.steps("../config/search.yaml")
        return self

    def add(self,name):
        self._params["name"] = name
        self.steps("../config/search.yaml")
        return self

    def is_choose(self,name):
        self._params["name"] = name
        return self.steps("../config/search.yaml")

    def reset(self,name):
        self._params["name"] = name
        self.steps("../config/search.yaml")

