from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_cms(driver, wait):
    cms_link = wait.until(EC.element_to_be_clickable((By.ID, "cms.sociowatch.in")))
    cms_link.click()
    print("🔁 Redirecting to cms.sociowatch.in...")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

def cms_login(driver, wait):
    email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email.send_keys("c-harshit.singh")
    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password.click()
    password.send_keys("5apVy1MViSrNrYz")

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "action")))
    login_button.click()
    print("✅ Logged in to CMS")
