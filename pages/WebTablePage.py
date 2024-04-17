from locators.WebTablePageLocators import WebTablePageLocators
from pages.Base_page import BasePage


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def create_user(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()