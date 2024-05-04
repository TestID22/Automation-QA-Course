import random

from selenium.webdriver.common.by import By


class FormPageLocators():

    NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES = (By.XPATH, f"//label[@for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_FILE = (By.XPATH, "//input[@id='uploadPicture']")