from tests.BaseTest import BaseTest


class TestLinksPage(BaseTest):

    def test_simple_link(self):
        self.links_page.open()
        href, link = self.links_page.check_new_tab_simple_link()
        assert href == link
        print(f"{href} == {link}")

    def test_broken_link(self):
        self.links_page.open()
        response_code = self.links_page.check_broken_link("https://demoqa.com/bad-request")
        assert response_code == 400
