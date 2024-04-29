from tests.BaseTest import BaseTest


class TestUploadAndDownload(BaseTest):

    def test_upload_file(self):
        self.upload_page.open()
        self.upload_page.upload_file()