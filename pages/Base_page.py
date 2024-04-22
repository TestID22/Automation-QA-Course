from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: object, url: object) -> object:
        self.driver = driver
        self.url = url
        self.wait = wait(driver,timeout=0)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=0):
        self.go_to_element(self.element_is_present(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=0):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=0):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=0):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

