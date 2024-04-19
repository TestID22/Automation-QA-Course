import time

from tests.BaseTest import BaseTest


class TestWebTablePage(BaseTest):


    def test_create_user(self):
        self.webtable_page.open()
        new_person = self.webtable_page.add_pesron()
        output = self.webtable_page.check_created_user()
        assert new_person in output

    #todo: write test for serching
    def test_search_created_person_in_the_table(self):
        pass