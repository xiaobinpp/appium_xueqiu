# -*- coding: utf-8 -*-
from page.app import App


class Test_Login:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        pass

    def test_userligin(self):
        finalpage = self.main.goto_mine().goto_login().input_account().input_passwd().click_login().get_toast()
        assert '成功' in finalpage

    def test_openaccount(self):
        pass



