from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found
import os
import time
import random
from dotenv import load_dotenv

# env file:
load_dotenv("LinkedIn_Request_Acceptor_Bot\.env")
linkedin_email=os.getenv("EMAIL")
linkedin_password=os.getenv("PASSWORD")
# print(f"Email: {linkedin_email}")
# print(f"Pass: {linkedin_password}")

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF linkedin page:
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

# close pop up:
try:
    driver.find_element(By.XPATH,'//*[@id="base-contextual-sign-in-modal"]/div/section/button/icon').click()
except NoSuchElementException:
    print("No pop-up found, proceeding.")


# SIGN IN:
time.sleep(5)       #loading time
email_input=driver.find_element(By.NAME,"session_key")
email_input.click()
email_input.send_keys(linkedin_email,Keys.TAB)
password_input=driver.find_element(By.NAME,"session_password")
password_input.send_keys(linkedin_password,Keys.ENTER)

time.sleep(25)       #loading time

# Accept:
acceptButtons = driver.find_elements(By.CLASS_NAME,"artdeco-button--secondary")

if not acceptButtons:
    print("No buttons found.")

for btn in acceptButtons:
    try:
        btn.click()
        time.sleep(0.5)
    except Exception as e:
        print(f"Error clicking button: {e}")
time.sleep(3)

print("Accepted all🥳!!")

# driver.quit()