from locators.CheckBoxPageLocators import CheckBoxPageLocators
from pages.Base_page import BasePage


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_three(self):
        self.element_is_present(self.locators.HOME_CHECKBOX).click()