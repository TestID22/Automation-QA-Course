import time

import requests

from locators.LinksPageLocators import LinksPageLocators
from pages.Base_page import BasePage


class LinksPage(BasePage):

    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    def check_broken_link(self, url):
        return requests.get(url).status_code
