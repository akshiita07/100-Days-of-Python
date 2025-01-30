GUARANTEED_DOWNLOAD=150
GUARANTEED_UPLOAD=10
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found
import os
import time
from dotenv import load_dotenv

# env file:
load_dotenv("Day51_Twitter_Complaint_Bot/.env")
email_id=os.getenv("EMAIL")
password=os.getenv("PASSWORD")
print(f"Email: {email_id}")

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF speedTest page:
driver.get("https://www.speedtest.net/")
time.sleep(5)

# click on go button:
try:
    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
except NoSuchElementException:
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
    
time.sleep(20)

download_speed=driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

upload_speed=driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

print(f"Your download speed is: {download_speed}")
print(f"Your upload speed is: {upload_speed}")

time.sleep(100)
# URL OF TWITTER page:
driver.get("https://tinder.com/app/recs")