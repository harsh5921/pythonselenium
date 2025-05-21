from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.check_url import check_url

def check_sidebar_links(driver, wait):
    try:
        print("🔍 Collecting all the links from the sidebar...")
        side_nav = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "side-nav")))
        links = side_nav.find_elements(By.TAG_NAME, "a")
        link_urls = [link.get_attribute("href") for link in links]

        if link_urls:
            print(f"✅ Found {len(link_urls)} links:")
            for url in link_urls:
                status = check_url(url)
                print(f"{url}: {status}")
        else:
            print("❌ No links found in the sidebar.")
    except Exception as e:
        print(f"❌ Error reading sidebar links: {e}")
