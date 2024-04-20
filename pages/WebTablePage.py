import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.WebTablePageLocators import WebTablePageLocators
from pages.Base_page import BasePage


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    #todo: Ask Max and Aleksei: a lot of code - maybe it can be simplified
    def add_person(self):
        '''Generate random data via @dataclass and Faker lib'''
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_created_user(self):
        table = self.elements_are_present(self.locators.PERSON_INFO)
        user_info = []
        for user in table:
            user_info.append(user.text.splitlines())
        return user_info

    def search_user(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)


    def check_search_user(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()