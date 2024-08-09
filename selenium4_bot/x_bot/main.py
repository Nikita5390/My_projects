import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from proxy_settings import get_chromedriver

load_dotenv()

pass_x = os.getenv('PASS_X')
new_pass = os.getenv('NEW_PASS')

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


"""
if you use PROXY

driver = get_chromedriver(use_proxy=True,
                          user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
"""


def change_password():
    try:
        driver.get('https://x.com/settings/password')
        time.sleep(5)

        curr_pasw = driver.find_element(By.NAME, 'current_password')
        curr_pasw.clear()
        curr_pasw.send_keys(f"{pass_x}")

        new_pasw = driver.find_element(By.NAME, 'new_password')
        new_pasw.clear()
        new_pasw.send_keys(f"{new_pass}")

        conf_pasw = driver.find_element(By.NAME, 'password_confirmation')
        conf_pasw.clear()
        conf_pasw.send_keys(f"{new_pass}")
        time.sleep(5)
        save_button = driver.find_element(By.XPATH, "//div[@role='button']").click()

    except Exception as ex:
        print(ex)


def retweet_post():
    try:
        driver.get('https://x.com/home')
        time.sleep(5)

        retweet_button = driver.find_element(By.XPATH, '//div[@data-testid="retweet"]')
        retweet_button[0].click()

    except Exception as ex:
        print(ex)


def main():
    try:
        change_password()
        retweet_post()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
