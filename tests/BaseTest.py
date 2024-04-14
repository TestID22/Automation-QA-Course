import pytest

from config.Links import Links
from pages.CheckBoxPage import CheckBoxPage
from pages.TextBoxPage import TextBoxPage


class BaseTest:

    text_box_page: TextBoxPage
    check_box_page: CheckBoxPage
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box_page = TextBoxPage(driver, Links.TEXT_BOX_PAGE)
        request.cls.check_box_page = CheckBoxPage(driver, Links.CHECK_BOX_PAGE)