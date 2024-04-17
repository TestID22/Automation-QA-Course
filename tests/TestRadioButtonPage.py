import time

from tests.BaseTest import BaseTest


class TestRadioButtonPage(BaseTest):

    def test_check_radiobutton(self):
        self.radiobutton_page.open()
        self.radiobutton_page.click_on_the_radio_button('yes')
        output = self.radiobutton_page.get_checked_radiobutton()
        assert output == "Yes"
        self.radiobutton_page.click_on_the_radio_button('impressive')
        output = self.radiobutton_page.get_checked_radiobutton()
        assert output == "Impressive"
        self.radiobutton_page.click_on_the_radio_button('no')
        output = self.radiobutton_page.get_checked_radiobutton()
        assert output == "No", 'there is a bug - button is not clicable'