from datetime import time
from time import sleep

from selenium.webdriver import Keys
from generator.generator import generated_person, file_generator
from locators.FormPageLocators import FormPageLocators
from pages.Base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form(self):
        person = next(generated_person())
        path, filename = file_generator()
        self.element_is_visible(self.locators.NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile_number) #todo: write generaTOR
        self.element_is_visible(self.locators.SUBJECT).send_keys("Hindi")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        sleep(5)
