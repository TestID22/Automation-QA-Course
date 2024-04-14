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
        self.text_box_page.fill_all_fields()
        output_name, output_email, output_current_adress, output_permanent_adress = self.text_box_page.check_filled_form()
        print(output_name, output_email, output_current_adress, output_permanent_adress)
