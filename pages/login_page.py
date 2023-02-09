from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://b2c.passport.rt.ru/account_b2c/login"
        self.username_input = driver.find_element_by_name("username")
        self.password_input = driver.find_element_by_name("password")

    def open(self):
        self.driver.get(self.url)

    def input_username(self, username):
        self.username_input.clear()
        self.username_input.send_keys(username)

    def input_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def get_username(self):
        return self.username_input.get_attribute("value")

    def get_password(self):
        return self.password_input.get_attribute("value")

def setup_module(module):
    options = Options()
    options.headless = True
    module.driver = webdriver.Chrome(options=options)

def teardown_module(module):
    module.driver.quit()

def test_site_status_code():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.driver.current_url == login_page.url
    driver.quit()

def test_form_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("test_username")
    login_page.input_password("test_password")
    assert login_page.get_username() == "test_username"
    assert login_page.get_password() == "test_password"
    time.sleep(3) # add sleep to view execution
    driver.quit()
