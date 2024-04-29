from pages.Base_page import BasePage
from locators.UploadAndDownloadPageLocators import UploadAndDonwloadPageLocators
from generator.generator import file_generator

class UploadAndDownloadPage(BasePage):

    locators = UploadAndDonwloadPageLocators()

    def upload_file(self):
        path, name = file_generator()
        print(name, path)