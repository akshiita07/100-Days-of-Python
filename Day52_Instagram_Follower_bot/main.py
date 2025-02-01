from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found
import os
import time
import random
from dotenv import load_dotenv

# env file:
load_dotenv("Day52_Instagram_Follower_bot/.env")
username_instagram=os.getenv("USERNAMEINSTAGRAM")
password=os.getenv("PASSWORD")
print(f"Username fetched from env: {username_instagram}")

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF instagram page:
driver.get("https://www.instagram.com/")
time.sleep(2)

# username:
driver.find_element(By.NAME,"username").click()
driver.find_element(By.NAME,"username").send_keys(username_instagram)
driver.find_element(By.NAME,"username").send_keys(Keys.TAB)

# password
driver.find_element(By.NAME,"password").click()
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)
time.sleep(5)

# do not save login info:
try:
    driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]").click()
except NoSuchElementException:
    print("Cannot find not now button")
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]").click()
time.sleep(3)

# URL OF the page we wish to get followers from:
driver.get("https://www.instagram.com/chefsteps/")
time.sleep(4)

try:
    driver.find_element(By.XPATH, "//a[@href='/chefsteps/followers/']").click()
except NoSuchElementException:
    print("Cannot find FOLLOWERS button using link text")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/chefsteps/followers/']").click()
time.sleep(5)

# scroll:
followerBox=driver.find_element(By.XPATH, "//div[@role='dialog']//div[contains(@class, 'x1dm5mii')]")

for _ in range(5):
    # remember: elementsss because many such btns have to be selected
    followButtons = driver.find_elements(By.XPATH, "//button[contains(., 'Follow')]")

    if not followButtons:
        print("No Follow buttons found.")
    
    for btn in followButtons:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", btn)
            btn.click()
            time.sleep(random.randint(2, 5))
        except Exception as e:
            print(f"Error clicking button: {e}")
    # scoll down:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followerBox)
    time.sleep(3)

print("Followed all🥳!!")