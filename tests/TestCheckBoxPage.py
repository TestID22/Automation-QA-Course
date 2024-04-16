import time

from tests.BaseTest import BaseTest


class TestCheckBoxpage(BaseTest):

    def test_open_three(self):
        self.check_box_page.open()
        self.check_box_page.open_full_list()
        self.check_box_page.check_random_checkbox()
        checked_items = self.check_box_page.collect_all_checked_items()
        output_data = self.check_box_page.get_output_result()
        assert checked_items == output_data, "strings do not match"
