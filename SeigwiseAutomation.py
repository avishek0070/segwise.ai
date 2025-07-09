import os
import time
import logging

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def main():
    load_dotenv()
    EMAIL = os.getenv("SEGWISE_EMAIL")
    PASSWORD = os.getenv("SEGWISE_PASSWORD")
    if not EMAIL or not PASSWORD:
        raise RuntimeError("Please set SEGWISE_EMAIL & SEGWISE_PASSWORD in your .env")

    # -----------------------------------------------------------------------------
    # 2. Configure logging
    # -----------------------------------------------------------------------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # -----------------------------------------------------------------------------
    # 3. Start Chrome WebDriver
    # -----------------------------------------------------------------------------
    opts = Options()
    # opts.add_argument("--headless")  # Uncomment to run without opening a window
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )
    wait = WebDriverWait(driver, 15)

    try:
        # -----------------------------------------------------------------------------
        # 4. Open Segwise login
        # -----------------------------------------------------------------------------
        driver.get("https://auth.segwise.ai/en/login")
        logging.info("Opened Segwise login page")

        # -----------------------------------------------------------------------------
        # 5. Wait for form inputs to render
        # -----------------------------------------------------------------------------
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        time.sleep(0.5)

        # -----------------------------------------------------------------------------
        # 6. Fill email
        # -----------------------------------------------------------------------------
        try:
            email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        except NoSuchElementException:
            email_field = driver.find_element(By.CSS_SELECTOR, "input[type='text'], input[type='email']")
        email_field.clear()
        email_field.send_keys(EMAIL)
        logging.info("Entered email")

        # -----------------------------------------------------------------------------
        # 7. Fill password
        # -----------------------------------------------------------------------------
        try:
            pw_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        except NoSuchElementException:
            pw_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        pw_field.clear()
        pw_field.send_keys(PASSWORD)
        logging.info("Entered password")

        # -----------------------------------------------------------------------------
        # 8. Click “Log in with email”
        # -----------------------------------------------------------------------------
        login_btn = driver.find_element(
            By.XPATH,
            "//button[contains(normalize-space(.), 'Log in with email')]"
        )
        old_url = driver.current_url
        login_btn.click()
        logging.info("Clicked login button")

        # -----------------------------------------------------------------------------
        # 9. Wait for URL to change off /login
        # -----------------------------------------------------------------------------
        try:
            wait.until(EC.url_changes(old_url))
            logging.info(f"URL changed to: {driver.current_url}")
        except TimeoutException:
            logging.warning(f"URL did not change from {old_url} within timeout")

        # -----------------------------------------------------------------------------
        # 10. Navigate to QA Assignment dashboard
        # -----------------------------------------------------------------------------
        dash_url = (
            "https://ua.segwise.ai/qa_assignment/home"
            "?report_date=2024-10-15&preset=last_7_days"
        )
        driver.get(dash_url)
        logging.info(f"Navigated to dashboard: {dash_url}")

        # -----------------------------------------------------------------------------
        # 11. Handle “Switch App” modal if it appears
        # -----------------------------------------------------------------------------
        try:
            switch_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Switch App']")
            ))
            switch_btn.click()
            logging.info("Clicked ‘Switch App’")
            time.sleep(1)
        except TimeoutException:
            logging.info("No ‘Switch App’ modal appeared — continuing")

        # -----------------------------------------------------------------------------
        # 12. Wait for “Search modules” input
        # -----------------------------------------------------------------------------
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Search modules']")
        ))
        logging.info("‘Search modules’ is visible")

        # -----------------------------------------------------------------------------
        # 13. Assert “Cost Per Install” card is present
        # -----------------------------------------------------------------------------
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(., 'Cost Per Install')]")
        ))
        logging.info("‘Cost Per Install’ card is present — you’re on the right page")
        input("\n✅ Automation done. Press Enter to close the browser and exit…")

    finally:
        driver.quit()
        logging.info("Browser closed")

if __name__ == "__main__":
    main()
