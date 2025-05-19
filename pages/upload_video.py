from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def upload_video(driver, wait):
    # Click on the video upload tab
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/media-video']")))
    print("Video tab button found")
    element.click()

    # Click the floating upload button
    try:
        upload = wait.until(EC.element_to_be_clickable((By.ID, "floatingButton")))
        print("Upload button found. Trying normal click...")
        upload.click()
    except Exception:
        print("⚠️ Normal click failed. Trying JavaScript click...")
        driver.execute_script("document.getElementById('floatingButton').click()")

    upload_section = wait.until(EC.presence_of_element_located((By.ID, "uploadvideo")))
    print("✅ Upload section found")

    # Step 2: Locate the <input type="file"> inside the upload section
    file_input = upload_section.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    print("file button found")

    # Provide the full path to the file
    file_input.send_keys("C:\\Users\\acer\\Downloads\\1747307046-Open-for-All--Navbharat-Shorts---23-.mp4")
    print("file input sent")

    # Wait for upload to complete (adjust time or implement proper wait)
    time.sleep(10)
    print("✅ Video(s) uploaded!")
