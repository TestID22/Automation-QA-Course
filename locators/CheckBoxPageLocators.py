from selenium.webdriver.common.by import By


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.XPATH, "//*[@class='rct-title']")
    CHECKED_ITEMS_LIST = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    TITLES_OF_CHECKED_LIST = (By.XPATH, "//*[@class='rct-icon rct-icon-check']/../../span[@class='rct-title']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")
