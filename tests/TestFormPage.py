from tests.BaseTest import BaseTest


class TestFormPage(BaseTest):

    def test_creation_of_user(self):
        self.form_page.open()
        person = self.form_page.fill_form()
        output = self.form_page.get_data_from_the_table()
        print(output)
        print(person)
        assert output[0] == person.first_name + " " + person.last_name