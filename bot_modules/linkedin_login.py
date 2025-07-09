import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

# Load credentials from .env file
load_dotenv()

USERNAME = os.getenv("LINKEDIN_USERNAME")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Open Chrome browser
driver = uc.Chrome()

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Fill in username and password
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)

# Click login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

print("✅ Logged into LinkedIn successfully!")