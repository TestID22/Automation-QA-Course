import time

from locators.DynamicProperiesPageLocators import DynamicPropertiesPageLocators
from pages.Base_page import BasePage

class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesPageLocators()

    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(6) #TODO:for myself in the future wtf?! REWRITE DUDE!!!
        color_after = color_button.value_of_css_property("color")
        return color_button_before, color_after

    def check_enable_button(self):
        try:
            enable_button = self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutError:
            return False
        return True

    def check_if_the_button_is_available_after_5_sec(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_BUTTON)
        except TimeoutException:
            return False
        return True
