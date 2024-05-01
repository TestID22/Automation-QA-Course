import base64
import os
import random

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

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute("href")
        link_b = base64.b64decode(link)
        path_name_file = rf'd:\file{random.randint(1, 100000)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        return check_file