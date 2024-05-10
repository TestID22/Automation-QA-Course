from pages.Base_page import BasePage
from locators.BrowserWindowPageLocators import BrowserWindowPageLocators


class BrowserWindowPage(BasePage):

    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEWTAB_BUTTON).click()

