from generator.generator import generated_person
from locators.WebTablePageLocators import WebTablePageLocators
from pages.Base_page import BasePage


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def create_user(self):
        person_info = next(generated_person())
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(person_info.full_name)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_info.email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_info.age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person_info.salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person_info.department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
