from selenium.webdriver.common.by import By


class BrowserWindowPageLocators():


    NEWTAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEWWINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEWWINDOW_MESSAGE = (By.XPATH, "//button[@id='messageWindowButton']")
