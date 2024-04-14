import random

from locators.CheckBoxPageLocators import CheckBoxPageLocators
from pages.Base_page import BasePage


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_present(self.locators.EXPAND_ALL_BUTTON).click()

    def check_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        item = item_list[random.randint(1, 15)]
        self.go_to_element(item)
        item.click()
        print(item.text)