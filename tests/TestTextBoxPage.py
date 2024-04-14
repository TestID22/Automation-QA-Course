import pytest


#todo: Create data generator
#todo: add faker
#todo: add links class
from generator.generator import generated_person
from tests.BaseTest import BaseTest


class TestTextBoxPage(BaseTest):

    @pytest.mark.smoke
    def test_create_user(self):
        self.text_box_page.open()
        full_name, email, current_address, permanent_address = self.text_box_page.fill_all_fields()
        output_name, output_email, output_current_address, output_permanent_address = self.text_box_page.check_filled_form()
        assert full_name == output_name
        assert email == output_email
        assert current_address.replace('\n', ' ') == output_current_address
        assert permanent_address.replace('\n', ' ') == output_permanent_address

