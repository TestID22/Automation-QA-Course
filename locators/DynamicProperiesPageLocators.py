from selenium.webdriver.common.by import By


class DynamicPropertiesPageLocators:

    COLOR_CHANGE_BUTTON = (By.XPATH, "//button[@id='colorChange']")
    ENABLE_BUTTON = (By.XPATH, "//button[@id='enableAfter']")
    VISIBLE_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")