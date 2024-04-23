from tests.BaseTest import BaseTest


class TestButtonsPage(BaseTest):


    def test_click(self):
        self.button_page.open()
        self.button_page.click_on_dynamic_button()
        output = self.button_page.check_if_dynamic_button_clicked()
        assert output == "You have done a dynamic click"