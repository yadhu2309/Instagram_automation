from selenium import webdriver
from selenium.webdriver.common.by import By
from config import USERNAME,PASSWORD,USERNAMES
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(
    options=options,
    executable_path='C:\Chromedriver\chromedrive')

browser.get('https://www.instagram.com')
time.sleep(2)


browser.find_element(By.NAME,'username').send_keys(USERNAME)
time.sleep(2)

browser.find_element(By.NAME,'password').send_keys(PASSWORD)
time.sleep(2)

browser.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
time.sleep(2)

for user in USERNAMES:
    time.sleep(1)
    browser.get(f'https://www.instagram.com/{user}')
    time.sleep(2)
    print(user)

time.sleep(2)
browser.close()
