from selenium.webdriver.common.by import By


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")