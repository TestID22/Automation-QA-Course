import random

from selenium.webdriver.common.by import By


class FormPageLocators():

    NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'id="dateOfBirthInput"')
    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES = (By.XPATH, f"//label[@for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_FILE = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    STATE_DIV = (By.XPATH, "//div[@id='state']")
    STATE_INPUT = (By.XPATH, "//input[@id='react-select-3-input']")
    CITY_DIV = (By.XPATH, "//div[@id='city']")
    CITY_INPUT = (By.XPATH, "//input[@id='react-select-4-input']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #output person
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")