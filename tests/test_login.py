import pytest
import allure
from utils.driver_setup import setup_driver
from pages.login_page import LoginPage

@allure.feature("Login Flow")
@allure.story("User logs in with valid credentials and OTP")
def test_valid_login():
    driver, wait = setup_driver()
    login_page = LoginPage(driver, wait)

    try:
        with allure.step("Enter credentials and OTP"):
            otp = input("Enter OTP: ")
            login_page.login("c-harshit.singh@timesgroup.com", "5apVy1MViSrNrYz", otp)
        with allure.step("Verify login success"):
            assert "https://safenet.timesnetwork.in/#/apps" in driver.page_source or driver.current_url
    finally:
        driver.quit()
