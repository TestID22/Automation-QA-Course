from locators.ButttonsPageLocators import ButtonsPageLocators
from pages.Base_page import BasePage


class ButtonsPage(BasePage):
    
    locators = ButtonsPageLocators()

    # TODO: rewrite into one func
    def click_on_dynamic_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def check_if_dynamic_button_clicked(self):
        return self.element_is_present(self.locators.OUTPUT_CLICK_ME).text

    def click_on_right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHTCLICK_BUTTON))

    def check_if_right_click_button_is_clicked(self):
        return self.element_is_present(self.locators.OUTPUT_RIGHTCLICK).text

    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLECLICK_BUTTON))

    def check_if_double_click_button_is_clicked(self):
        return self.element_is_present(self.locators.DOUBLECLICK_BUTTON).text