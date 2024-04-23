from locators.ButttonsPageLocators import ButtonsPageLocators
from pages.Base_page import BasePage


class ButtonsPage(BasePage):
    
    locators = ButtonsPageLocators()

    def click_on_dynamic_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def check_if_dynamic_button_clicked(self):
        return self.element_is_present(self.locators.OUTPUT_CLICK_ME).text
