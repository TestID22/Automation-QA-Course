# Automation-QA-Course"

Test site - https://demoqa.com/
Workflow

Create Project (activate venv) .\venv\scripts\activate
Import libraries - pip install pytest selenium webdriver_manager
pip freeze>requirenments.txt
Create conftest.py
import services from selenium import webdriver from selenium.webdriver.chrome.service import Service
import webdriverWait to BasePage from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions
Created config folder with Links Class
Created first Base page open, isopened and
Login page object page was inherited from Base page LOGIN_FIELD = ("xpath", "//input[@name='username']") PASSWORD_FIELD = ("xpath", "//input[@name='password']")