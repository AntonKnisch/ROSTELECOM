# login_page.py

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://b2c.passport.rt.ru/account_b2c/login"
        self.tabs_selector = ".tabs .tab"
        self.form_inputs_selector = ".form-input"
        self.default_tab_selector = ".tabs .tab.selected"
        self.product_slogan_selector = ".product-slogan"
        self.customer_support_selector = ".customer-support"

    def open(self):
        self.driver.get("https://b2c.passport.rt.ru/account_b2c/login")

    def get_username(self):
        username_input = self.driver.find_element(*self.username_input)
        return username_input.get_attribute("value")

    def get_password(self):
        password_input = self.driver.find_element(*self.password_input)
        return password_input.get_attribute("value")

    def input_username(self, username):
        username_input = self.driver.find_element(*self.username_input)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(password)

    def get_tab_titles(self):
        tabs = self.driver.find_elements_by_css_selector(self.tabs_selector)

