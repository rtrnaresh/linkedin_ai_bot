from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def apply_to_jobs(driver):
    print("🔍 Searching and applying to jobs...")
    driver.get("https://www.linkedin.com/jobs")
    time.sleep(5)

    search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search jobs']")
    search_box.clear()
    search_box.send_keys("Software Engineer")  # Replace with keyword from resume parser
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")[:5]

    for job in jobs:
        try:
            job.click()
            time.sleep(3)
            easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            easy_apply.click()
            time.sleep(2)
            # Add more form automation if needed
            print("✅ Applied to a job")
        except Exception as e:
            print(f"Skipped one job: {e}")
        time.sleep(2)
