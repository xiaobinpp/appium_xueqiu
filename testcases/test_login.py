# -*- coding: utf-8 -*-
import pytest
import yaml

from page.app import App


class Test_Login:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.end()

    # @pytest.mark.skip
    def test_userligin(self):
        # finalpage = self.main.goto_mine().goto_login().input_account().input_passwd().click_login().get_toast()
        # assert '成功' in finalpage
        self.main.goto_mine()

    @pytest.mark.skip
    def test_openaccount(self):
        pass

    @pytest.mark.skip
    @pytest.mark.parametrize("param1,param2",yaml.safe_load(open('../config/test_param.yaml')))
    def test_param(self,param1,param2):
        print(param1,param2)

