from selenium.webdriver.common.by import By


class FormPageLocators():

    NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    MALE_CHECKBOX = (By.XPATH, "//input[@id='gender-radio-1']")