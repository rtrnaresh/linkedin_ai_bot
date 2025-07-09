from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bot_modules.resume_parser import parse_resume

def apply_to_jobs(driver):
    print("📄 Parsing resume to get keywords...")
    resume_data = parse_resume("Naresh Resume.pdf")
    search_keywords = resume_data["roles"] + resume_data["skills"]

    if not search_keywords:
        print("⚠️ No keywords found in resume. Aborting job search.")
        return

    # Use first keyword for now
    keyword = search_keywords[0]
    print(f"🔍 Searching jobs for: {keyword}")
    
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(5)

    # Enter job title
    try:
        job_search = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search jobs']")
        job_search.clear()
        job_search.send_keys(keyword)
        job_search.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print(f"❌ Error in search input: {e}")
        return

    # Apply to jobs
    jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")[:5]
    
    for index, job in enumerate(jobs):
        try:
            print(f"🔗 Opening job #{index+1}")
            job.click()
            time.sleep(3)

            easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            easy_apply.click()
            time.sleep(3)

            # Try submitting application (works for 1-click ones)
            submit_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Submit application')]")
            submit_button.click()
            print("✅ Successfully applied!\n")

            # Wait after applying
            time.sleep(5)
        except Exception as e:
            print(f"⏭️ Skipped job #{index+1}: {e}")
            time.sleep(2)
