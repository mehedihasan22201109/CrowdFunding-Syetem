from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome Driver Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the About page
driver.get("http://127.0.0.1:8000/about/")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome driver setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the local Django site
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()
time.sleep(3)

print("\n--- Crowdfunding Homepage Selenium Test ---\n")

try:
    # ✅ Test 1: Page Title visible
    hero_title = driver.find_element(By.CLASS_NAME, "crowdfunding-hero-title")
    print("✅ Hero Title Found:", hero_title.text)

    # ✅ Test 2: Register button visible for unauthenticated users
    try:
        register_button = driver.find_element(By.CLASS_NAME, "register-btn")
        print("✅ Register Button Found:", register_button.text)
    except NoSuchElementException:
        print("⚠ Register Button Not Found (User may be logged in)")

    # ✅ Test 3: Hero background image exists
    hero_image = driver.find_element(By.TAG_NAME, "img")
    print("✅ Hero Image Found with src:", hero_image.get_attribute("src"))

    # ✅ Test 4: Blog Section Exists
    blogs = driver.find_elements(By.CLASS_NAME, "blog-eventd")
    print(f"✅ Found {len(blogs)} Blog Cards.")
    for i, blog in enumerate(blogs):
        title = blog.find_element(By.CLASS_NAME, "blog-eventd-title").text
        print(f"   → Blog {i+1} Title:", title)

    # ✅ Test 5: Video Section Present
    video_tag = driver.find_element(By.TAG_NAME, "video")
    print("✅ Video Section Found:", video_tag.get_attribute("src"))

    # ✅ Test 6: Stats Section visible
    stats_section = driver.find_element(By.CLASS_NAME, "white-counter-section")
    print("✅ Stats Section Found.")

    # ✅ Test 7: Counter Numbers
    numbers = stats_section.find_elements(By.CLASS_NAME, "stats-number")
    print("   → Found Counter Numbers:", [num.text for num in numbers])

    print("\n🎉 All visible element tests passed successfully!\n")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    time.sleep(2)
    
    driver.quit()

driver.maximize_window()
time.sleep(2)