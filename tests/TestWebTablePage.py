import random
from tests.BaseTest import BaseTest

class TestWebTablePage(BaseTest):

    def test_create_user(self):
        self.webtable_page.open()
        new_person = self.webtable_page.add_person()
        output = self.webtable_page.check_created_user()
        assert new_person in output

    def test_search_created_person_in_the_table(self):
        self.webtable_page.open()
        new_user = self.webtable_page.add_person()
        self.webtable_page.search_user(new_user[0])
        table_result = self.webtable_page.check_created_user()
        assert new_user in table_result


    def test_change_user_profile(self):
        self.webtable_page.open()
        new_user = self.webtable_page.add_person()[random.randint(0, 5)]
        self.webtable_page.search_user(new_user)
        age = self.webtable_page.edit_user()
        updated_person = self.webtable_page.check_search_user()
        assert age in updated_person, 'ages are not match'


    def test_delete_user(self):
        self.webtable_page.open()
        first_name = self.webtable_page.add_person()[0]
        self.webtable_page.search_user(first_name)
        self.webtable_page.delete_user()
        data = self.webtable_page.check_deleted_user()
        assert data == "No rows found"
