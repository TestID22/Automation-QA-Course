import time

from tests.BaseTest import BaseTest


class TestRadioButtonPage(BaseTest):

    def test_check_radiobutton(self):
        self.radiobutton_page.open()
        checked_radiobutton = self.radiobutton_page.check_radiobutton()
        output_radiobutton = self.radiobutton_page.get_checked_radiobutton()
        assert checked_radiobutton == output_radiobutton