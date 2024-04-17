from locators.RadioButtonPageLocators import RadioButtonPageLocators
from pages.Base_page import BasePage


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(choices[choice]).click()

    def get_checked_radiobutton(self):
        return self.element_is_visible(self.locators.OUTPUT_RESULT).text