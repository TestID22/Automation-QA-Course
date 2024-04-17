from selenium.webdriver.common.by import By


class RadioButtonPageLocators():
    YES_RADIOBUTTON = (By.XPATH, "//label[@class='custom-control-label' and @for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@class='custom-control-label' and @for='impressiveRadio']")
    NO_RADIOBUTTON = (By.XPATH, "//label[@class='custom-control-label disabled' and @for='noRadio']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")
