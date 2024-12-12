import os
import sys
import logging
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def find_chrome_path():
    """
    Find the path to Chrome executable on macOS
    """
    possible_browsers = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/local/bin/chrome",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser"
    ]
    
    # Check for browsers in PATH and file system
    for browser in possible_browsers:
        browser_name = os.path.basename(browser)
        if shutil.which(browser_name) or os.path.exists(browser):
            logger.info(f"Found browser at: {browser}")
            return browser
    
    # If no browser found, try to find Chrome via Homebrew
    homebrew_chrome = "/opt/homebrew/bin/google-chrome"
    if os.path.exists(homebrew_chrome):
        logger.info(f"Found Homebrew Chrome at: {homebrew_chrome}")
        return homebrew_chrome
    
    logger.error("No Chrome/Chromium browser found.")
    raise FileNotFoundError("Chrome/Chromium browser not found. Please install a browser.")

def scrape_x_thread(url):
    """
    Scrape the content of an X (Twitter) thread using Selenium
    
    Args:
        url (str): Full URL of the X thread
    
    Returns:
        str: Extracted text content of the thread
    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Find Chrome path
    try:
        chrome_path = find_chrome_path()
        chrome_options.binary_location = chrome_path
    except Exception as e:
        logger.error(f"Error finding browser: {e}")
        return None
    
    # Use the ChromeDriver path
    chromedriver_path = "/opt/homebrew/bin/chromedriver"
    service = Service(chromedriver_path)
    
    driver = None
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Set a page load timeout
        driver.set_page_load_timeout(30)  # Increased timeout
        
        # Navigate to the URL
        driver.get(url)
        
        # Scroll to load all tweets (if needed)
        ActionChains(driver).move_to_element(driver.find_element(By.TAG_NAME, 'body')).perform()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for tweet elements to be present
        wait = WebDriverWait(driver, 30)  # Increased timeout
        tweet_elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@data-testid='tweet']")
            )
        )
        
        # Extract text from tweet elements
        tweet_texts = []
        for tweet in tweet_elements:
            text = tweet.text.strip()
            if text:
                tweet_texts.append(text)
        
        # Combine tweets
        full_thread_text = "\n\n".join(tweet_texts)
        
        # Create filename
        filename = f"x_thread_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Source URL: {url}\n\n")
            f.write(full_thread_text)
        
        logger.info(f"Thread content saved to {filename}")
        return full_thread_text
    
    except TimeoutException:
        logger.error("Timeout while waiting for page elements")
        return None
    except WebDriverException as e:
        logger.error(f"WebDriver error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        # Always close the browser if it was opened
        if driver:
            try:
                driver.quit()
            except Exception as e:
                logger.error(f"Error closing driver: {e}")

# Example usage
def main():
    # Replace with the actual X thread URL you want to scrape
    thread_url = "https://x.com/FinanceYF5/status/1864222756377907708"
    result = scrape_x_thread(thread_url)
    
    if result is None:
        logger.error("Failed to scrape the thread.")
        sys.exit(1)

if __name__ == "__main__":
    main()
