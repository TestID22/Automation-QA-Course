import random
import time

from tests.BaseTest import BaseTest


class TestWebTablePage(BaseTest):


    def test_create_user(self):
        self.webtable_page.open()
        new_person = self.webtable_page.add_person()
        output = self.webtable_page.check_created_user()
        assert new_person in output

    #todo: Unsatable: improve search_user
    def test_search_created_person_in_the_table(self):
        self.webtable_page.open()
        new_user = self.webtable_page.add_person()
        self.webtable_page.search_user(new_user[0])
        table_result = self.webtable_page.check_created_user()
        assert new_user in table_result