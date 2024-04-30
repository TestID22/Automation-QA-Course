import os

from pages.Base_page import BasePage
from locators.UploadAndDownloadPageLocators import UploadAndDonwloadPageLocators
from generator.generator import file_generator

class UploadAndDownloadPage(BasePage):

    locators = UploadAndDonwloadPageLocators()

    def upload_file(self):
        path, name = file_generator()
        self.element_is_visible(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        file_name = self.element_is_present(self.locators.UPLOADED_FILE).text
        return path.split("\\")[-1], file_name.split("\\")[-1]


    #todo: Download_file func
    def download_file(self):
        pass