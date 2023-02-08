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
        self.driver.get(self.url)

    def get_tab_titles(self):
        tabs = self.driver.find_elements_by_css_selector(self.tabs_selector)
        return [tab.text for tab in tabs]

    def get_form_input_titles(self):
        forms = self.driver.find_elements_by_css_selector(self.form_inputs_selector)
        return [form.get_attribute("placeholder") for form in forms]

    def get_default_tab_text(self):
        default_tab = self.driver.find_element_by_css_selector(self.default_tab_selector)
        return default_tab.text

    def get_product_slogan(self):
        product_slogan = self.driver.find_element_by_css_selector(self.product_slogan_selector)
        return product_slogan.text

    def is_customer_support_displayed(self):
        customer_support = self.driver.find_element_by_css_selector(self.customer_support_selector)
        return customer_support.is_displayed()
