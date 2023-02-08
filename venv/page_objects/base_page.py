from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver, url, payload):
        self.driver = driver
        self.url = url
        self.payload = payload

    def open(self):
        self.driver.get(self.url + '?' + '&'.join(f'{k}={v}' for k,v in self.payload.items()))
        return self

    def is_status_code_200(self):
        return self.driver.title

    def is_redirected(self):
        return self.driver.current_url.startswith(self.payload['redirect_uri'])

    def enter_username(self, username):
        self.driver.find_element_by_name("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name("password").send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
