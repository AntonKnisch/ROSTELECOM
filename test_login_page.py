from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from login_page import LoginPage

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

def test_site_redirect():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.driver.current_url == "https://b2c.passport.rt.ru/account_b2c/login"
    driver.quit()

def test_tab_selections():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    tab_titles = login_page.get_tab_titles()
    assert tab_titles == ["Номер", "Почта", "Логин", "Лицевой счет"]
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
