from selenium.webdriver.common.by import By


class ButtonsPageLocators():

    DOUBLECLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHTCLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    #results

    OUTPUT_DOUBLECLICK = (By.XPATH, "//p[@id='doubleClickMessage']")
    OUTPUT_RIGHTCLICK = (By.XPATH, "//p[@id='rightClickMessage']")
    OUTPUT_CLICK_ME = (By.XPATH, "//p[@id='dynamicClickMessage']")