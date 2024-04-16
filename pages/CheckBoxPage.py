import random

from selenium.webdriver.common.by import By

from locators.CheckBoxPageLocators import CheckBoxPageLocators
from pages.Base_page import BasePage


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_present(self.locators.EXPAND_ALL_BUTTON).click()

    def check_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        check_list = random.sample(range(1,15), 5)
        for checkbox in check_list:
            self.go_to_element(item_list[checkbox])
            item_list[checkbox].click()

    def collect_all_checked_items(self):
        checked_items_list = self.elements_are_visible(self.locators.TITLES_OF_CHECKED_LIST)
        checked_items = []
        for item in checked_items_list:
            checked_items.append(item.text)
        return str(checked_items).replace(' ', '').capitalize().replace(".doc", '')

    def get_output_result(self):
        output_result = self.elements_are_present(self.locators.OUTPUT_RESULT)
        output_data = []
        for res in output_result:
            output_data.append(res.text)
        return str(output_data).replace(' ', '').lower()