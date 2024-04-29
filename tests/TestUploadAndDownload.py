import time

from tests.BaseTest import BaseTest


class TestUploadAndDownload(BaseTest):


    def test_upload_file(self):
        self.upload_page.open()
        path, file_name = self.upload_page.upload_file()
        assert path == file_name
