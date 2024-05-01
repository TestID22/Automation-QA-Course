from tests.BaseTest import BaseTest


class TestDynamicProperties(BaseTest):


    def test_change_button_color(self):
        self.dynamic_properties_page.open()
        color_before, color_after = self.dynamic_properties_page.check_changed_color()
        assert color_before != color_after
        print(color_after, color_before)


    def test_button_appearing(self):
        self.dynamic_properties_page.open()
        status = self.dynamic_properties_page.check_if_the_button_is_available_after_5_sec()
        assert status is True

    def test_button_enabling(self):
        self.dynamic_properties_page.open()
        button_status = self.dynamic_properties_page.check_enable_button()
        assert button_status is True