# -*- coding: utf-8 -*-
import pytest

from page.app import App


class Test_Search():
    def setup(self):
        self.app = App()
        self.search = self.app.start().goto_main().goto_market().goto_seacrh()

    def teardown(self):
        self.app.end()

    @pytest.mark.parametrize("name",["京东","阿里巴巴"])
    def test_search_add(self,name):
        self.search.search(name)
        if self.search.is_choose(name) is not None:
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)


