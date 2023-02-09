# test_registration_page.py

import pytest
from selenium import webdriver
from pages.regestration_page import RegistrationPage
from locators import RegistrationPageLocators

def test_registration_form_input():
    driver = webdriver.Chrome()
    registration_page = RegistrationPage(driver)
    registration_page.open()

    username = "test_username"
    email = "test_email@gmail.com"
    password = "test_password"

    registration_page.input_username(username)
    registration_page.input_email(email)
    registration_page.input_password(password)
    registration_page.submit()

    # Add asserts to check if the input was successful
    assert driver.find_element(*RegistrationPageLocators.USERNAME_INPUT).get_attribute("value") == username
    assert driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).get_attribute("value") == email
    assert driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).get_attribute("value") == password
