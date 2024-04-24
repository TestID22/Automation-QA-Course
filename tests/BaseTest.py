import pytest

from config.Links import Links
from pages.ButtonsPage import ButtonsPage
from pages.CheckBoxPage import CheckBoxPage
from pages.LinksPage import LinksPage
from pages.RadioButtonPage import RadioButtonPage
from pages.TextBoxPage import TextBoxPage
from pages.WebTablePage import WebTablePage


class BaseTest:

    text_box_page: TextBoxPage
    check_box_page: CheckBoxPage
    radiobutton_page: RadioButtonPage
    webtable_page: WebTablePage
    button_page: ButtonsPage
    links_page: LinksPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box_page = TextBoxPage(driver, Links.TEXT_BOX_PAGE)
        request.cls.check_box_page = CheckBoxPage(driver, Links.CHECK_BOX_PAGE)
        request.cls.radiobutton_page = RadioButtonPage(driver, Links.RADIO_BUTTON_PAGE)
        request.cls.webtable_page = WebTablePage(driver, Links.WEB_TABLE_PAGE)
        request.cls.button_page = ButtonsPage(driver, Links.BUTTONS_PAGE)
        request.cls.links_page = LinksPage(driver, Links.LINKS_PAGE)