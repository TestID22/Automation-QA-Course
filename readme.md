# Automation-QA-Course"

Test site - https://demoqa.com/
Workflow

1. Create Project (activate venv) .\venv\scripts\activate
2. Import libraries - pip install pytest selenium webdriver_manager
3. pip freeze>requirenments.txt
4. Create conftest.py
5.import services from selenium import webdriver from selenium.webdriver.chrome.service import Service
  import webdriverWait to BasePage from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions
6. Created config folder with Links Class
7. Created first Base page open - Common Methods are located here. 
8. Login page object page was inherited from Base page
   xpath samples = "LOGIN_FIELD = ("xpath", "//input[@name='username']") PASSWORD_FIELD = ("xpath", "//input[@name='password']")"
11. Added BaseTest class to provide all pages into other testclasses
12. Added Person Generator. It uses Faker + dataclass 
13. CheckBoxPage: Find child element .//ancestor::span[@class='rct-title'] 
