from tests.BaseTest import BaseTest


class TestButtonsPage(BaseTest):


    def test_click(self):
        self.button_page.open()
        self.button_page.click_on_dynamic_button()
        output = self.button_page.check_if_dynamic_button_clicked()
        assert output == "You have done a dynamic click"

    def test_right_click_button(self):
        self.button_page.open()
        self.button_page.click_on_right_click_button()
        output = self.button_page.check_if_right_click_button_is_clicked()
        assert output == "You have done a right click"

    def test_double_click(self):
        self.button_page.open()
        self.button_page.double_click()
        output = self.button_page.check_if_double_click_button_is_clicked()
        assert output == "Double Click Me"