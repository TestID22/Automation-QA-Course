import time

from tests.BaseTest import BaseTest


class TestUploadAndDownload(BaseTest):


    def test_upload_file(self):
        self.upload_page.open()
        path, file_name = self.upload_page.upload_file()
        assert path == file_name, "File has not been uploaded"


    def test_download_file(self):
        self.upload_page.open()
        file_status = self.upload_page.download_file()
        assert file_status == True, "File has not been downloaded"