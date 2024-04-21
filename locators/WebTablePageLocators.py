from selenium.webdriver.common.by import By


class WebTablePageLocators:

    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    #table
    PERSON_INFO = (By.XPATH, "//div[@class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@class='form-control']")
    DELETE_BUTTON =  (By.XPATH, "//span[@title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = ((By.XPATH, "//span[@title='Edit']"))