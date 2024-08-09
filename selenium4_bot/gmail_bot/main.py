import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from proxy_settings import get_chromedriver
import pickle

load_dotenv()

log_google = os.getenv('LOG_GOOGLE')
pass_google = os.getenv('PASS_GOOGLE')
new_pass = os.getenv('NEW_PASS')
new_name = os.getenv('NEW_NAME')
new_last_name = os.getenv('NEW_L_NAME')

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

"""
if you use PROXY

driver = get_chromedriver(use_proxy=True,
                          user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
"""


def login():
    try:
        driver.get(
            'https://accounts.google.com/v3/signin/identifier?checkedDomains=youtube&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&emr=1&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&hl=ru&ifkv=AdF4I77QCTR1e2XVhhCVh1_oQ4Ml_00qN2i79Wgvl8bNp9NyC5JfHSWA4KECxy0TkVd1EToKzzhf&osid=1&pstMsg=1&service=mail&flowEntry=AccountChooser')
        time.sleep(5)

        email_input = driver.find_element(By.ID, 'identifierId')
        email_input.clear()
        email_input.send_keys(f"{log_google}")
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)

        pass_input = driver.find_element(By.NAME, 'Passwd')
        pass_input.clear()
        pass_input.send_keys(f"{pass_google}")
        pass_input.send_keys(Keys.ENTER)
    except Exception as ex:
        print(ex)


def change_password():
    try:
        driver.get('https://myaccount.google.com/security?hl=ru&utm_source=OGB&utm_medium=act')
        time.sleep(5)

        pasw_input = driver.find_element(By.CSS_SELECTOR, '[aria-label="Пароль"]').click()
        time.sleep(5)

        """
        (save cookies:)
        pickle.dump(driver.get_cookies(), open(f"{x_phone}_cookies", "wb"))
        
        (add cookies:)
        for cookie in pickle.load(open(f"{x_phone}_cookies", "rb")):
        driver.add_cookie(cookie)
        
        """

        new_pasw = driver.find_element(By.NAME, 'password')
        new_pasw.clear()
        new_pasw.send_keys(f"{new_pass}")
        conf_pasw = driver.find_element(By.NAME, 'confirmation_password')
        conf_pasw.clear()
        conf_pasw.send_keys(f"{new_pass}")
        change_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Сменить пароль').click()

    except Exception as ex:
        print(ex)


def change_name():
    try:
        driver.get('https://myaccount.google.com/personal-info?hl=ru&utm_source=OGB&utm_medium=act')
        time.sleep(5)

        change_input = driver.find_element(By.ID, 'c6').click()
        time.sleep(5)
        change_input2 = driver.find_element(By.CSS_SELECTOR, '[aria-label="Изменить поле &quot;Имя&quot;"]').click()
        name = driver.find_element(By.ID, 'i7')
        name.send_keys(f"{new_name}")
        last_name = driver.find_element(By.ID, 'i12')
        last_name.send_keys(f"{new_last_name}")
        save_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Сохранить').click()



    except Exception as ex:
        print(ex)


def main():
    try:
        login()
        change_name()
        change_password()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
