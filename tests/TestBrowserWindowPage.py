import time

from tests.BaseTest import BaseTest


class TestBrowserWindowPage(BaseTest):


    def test_new_tab(self):
        self.new_tab_page.open()
        self.new_tab_page.check_opened_new_tab()
        time.sleep(2)