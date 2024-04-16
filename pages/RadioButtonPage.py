from locators.RadioButtonPageLocators import RadioButtonPageLocators
from pages.Base_page import BasePage


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        radiobutton_list = self.elements_are_visible(self.locators.RADIOBUTTONS_LIST)
        choice = {'yes': "",
                  'impressive': "",
                  'no': ""
        }

        def get_checked_radiobutton(self):
            return self.element_is_visible(self.locators.CHECKED_RADIOBUTTON).text