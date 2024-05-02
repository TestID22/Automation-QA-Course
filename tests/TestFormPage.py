from tests.BaseTest import BaseTest


class TestFormPage(BaseTest):

    def test(self):
        self.form_page.open()
        self.form_page.fill_form()