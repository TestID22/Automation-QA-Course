import time

from generator.generator import generated_person
from locators.FormPageLocators import FormPageLocators
from pages.Base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form(self):
        person = next(generated_person())
        self.element_is_present(self.locators.NAME_INPUT).send_keys(person.first_name)
        self.element_is_present(self.locators.LASTNAME_INPUT).send_keys(person.last_name)
        self.element_is_present(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_present(self.locators.MALE_CHECKBOX).click()
