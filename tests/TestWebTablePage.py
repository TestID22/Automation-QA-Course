import time

from tests.BaseTest import BaseTest


class TestWebTablePage(BaseTest):


    def test_create_user(self):
        self.webtable_page.open()
        self.webtable_page.create_user()
        time.sleep(6)