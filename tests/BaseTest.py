import pytest

from config.Links import Links
from pages.TextBoxPage import TextBoxPage


class BaseTest:

    text_box_page: TextBoxPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box_page = TextBoxPage(driver, Links.TEXT_BOX_PAGE)
