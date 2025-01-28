from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found
import os
import time
from dotenv import load_dotenv

# env file:
load_dotenv("Day49_Automated_Job_Application_Bot/.env")
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
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4130352892&f_AL=true&f_E=1&geoId=102713980&keywords=web%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# close pop up:
try:
    driver.find_element(By.XPATH,'//*[@id="base-contextual-sign-in-modal"]/div/section/button/icon').click()
except NoSuchElementException:
    print("No pop-up found, proceeding.")


# SIGN IN:
driver.find_element(By.LINK_TEXT,"Sign in").click()
# driver.find_element(By.CSS_SELECTOR,'#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button').click()
email_input=driver.find_element(By.NAME,"session_key")
email_input.click()
email_input.send_keys(linkedin_email,Keys.TAB)
password_input=driver.find_element(By.NAME,"session_password")
password_input.send_keys(linkedin_password,Keys.ENTER)

# Apply:
time.sleep(3)       #loading time
driver.find_element(By.ID,"ember54").click()
driver.find_element(By.ID,"ember1033").click()
driver.find_element(By.ID,"ember1033").click()
driver.find_element(By.ID,"ember1015").click()
driver.find_element(By.ID,"ember1025").click()
print("Application submitted.")

# driver.quit()