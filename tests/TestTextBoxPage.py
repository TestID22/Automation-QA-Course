import pytest


from generator.generator import generated_person
from tests.BaseTest import BaseTest


class TestTextBoxPage(BaseTest):

    @pytest.mark.smoke
    def test_create_user(self):
        self.text_box_page.open()
        full_name, email, current_address, permanent_address = self.text_box_page.fill_all_fields()
        output_name, output_email, output_current_address, output_permanent_address = self.text_box_page.check_filled_form()
        assert full_name == output_name , "full_name does not match"
        assert email == output_email , "email does not match"
        assert current_address.replace('\n', ' ') == output_current_address, "current address does not match"
        assert permanent_address.replace('\n', ' ') == output_permanent_address , "permanent address does not match"

