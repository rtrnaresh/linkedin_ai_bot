from bot_modules.linkedin_login import login_linkedin
from bot_modules.auto_reply import auto_reply_messages
from bot_modules.jobs import apply_to_jobs
from bot_modules.profile import update_profile
import schedule
import time

def run_bot():
    driver = login_linkedin()
    auto_reply_messages(driver)
    apply_to_jobs(driver)
    update_profile(driver)
    driver.quit()

schedule.every(2).hours.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(1)
