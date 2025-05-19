from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

def search_video(driver, wait):
    video = wait.until(EC.presence_of_element_located((By.ID, "mhsearch")))
    video.send_keys("1xb14pn5jz_w", Keys.ENTER)
    print("video found")
    time.sleep(10)
