import time

from tests.BaseTest import BaseTest


class TestCheckBoxpage(BaseTest):

    def test_open_three(self):
        self.check_box_page.open()
        self.check_box_page.open_three()
        time.sleep(5)