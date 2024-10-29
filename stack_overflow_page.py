import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def login():
    print("Logging into stackoverflow.com...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    try:
        driver.get("https://stackoverflow.com")
        driver.find_element(By.LINK_TEXT, "Log in").click()

        cookies_btn = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )

        cookies_btn.click()

        driver.find_element(By.ID, "email").send_keys(os.environ.get("STACK_OVERFLOW_EMAIL"))
        driver.find_element(By.ID, "password").send_keys(os.environ.get("STACK_OVERFLOW_PASSWORD"))
        driver.find_element(By.ID, "submit-button").click()

        user_profile_btn = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "user-profile-button"))
        )
        user_profile_btn.click()

        elem = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "flex--item.mb12.fs-headline2"))
        )
        assert os.environ['STACK_OVERFLOW_DISPLAY_NAME'] in elem.text
        print("Logged into stackoverflow.com and accessed profile page")

    except Exception as e:
        print("An error occurred while trying to access stackoverflow.com!", e)
    finally:
        driver.close()

if __name__ == "__main__":
    login() 

