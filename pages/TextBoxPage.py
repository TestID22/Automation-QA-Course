from generator.generator import generated_person
from locators.TextBoxPageLocators import TextBoxPageLocators
from pages.Base_page import BasePage


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info =  next(generated_person())
        first_name = person_info.first_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return first_name, email, current_address, permanent_address


    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address