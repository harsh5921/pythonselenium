from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Logging in to Safenet portal")
    def login(self, username, password, otp_code):
        self.driver.get("https://safenet.timesnetwork.in/#/login")
        self.wait.until(lambda d: d.find_element(By.ID, "username")).send_keys(username)
        self.wait.until(lambda d: d.find_element(By.ID, "password")).send_keys(password)
        self.wait.until(lambda d: d.find_element(By.ID, "cal-login-button")).click()
        self.wait.until(lambda d: d.find_element(By.ID, "cal-token-verify-code")).send_keys(otp_code)
        self.wait.until(lambda d: d.find_element(By.ID, "cal-token-verify-btn")).click()
