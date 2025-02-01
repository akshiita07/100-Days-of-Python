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
username_twitter=os.getenv("USERNAMETWITTER")
password=os.getenv("PASSWORD")
email=os.getenv("EMAIL")
print(f"Username fetched from env: {username_twitter}")

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF speedTest page:
driver.get("https://www.speedtest.net/")
time.sleep(2)

# accept cookies:
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

# click on go button:
try:
    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
except NoSuchElementException:
    print("Go button was not found")
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
    
time.sleep(50)

download_speed=driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

upload_speed=driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

print(f"Your download speed is: {download_speed}")
print(f"Your upload speed is: {upload_speed}")

print("Completed speed test now moving to twitter")
time.sleep(3)

# URL OF TWITTER page:
driver.get("https://x.com/home")
time.sleep(5)

# base_window = driver.current_window_handle
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)
# driver.switch_to.window(base_window)
# print(driver.title)

# sign-into twitter:
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a').click()
time.sleep(5)

# username:
driver.find_element(By.NAME,"text").click()
driver.find_element(By.NAME,"text").send_keys(username_twitter)
driver.find_element(By.NAME,"text").send_keys(Keys.ENTER)
time.sleep(3)

try:
    # if email asked:
    driver.find_element(By.NAME,"text").click()
    driver.find_element(By.NAME,"text").send_keys(email)
    driver.find_element(By.NAME,"text").send_keys(Keys.ENTER)
    time.sleep(3)
    # password
    driver.find_element(By.NAME,"password").click()
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)
    time.sleep(5)
except NoSuchElementException:
    # password
    driver.find_element(By.NAME,"password").click()
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)
    time.sleep(5)

# write tweet:
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').click()
time.sleep(2)

message=f"Hey internet provider, why is my internet speed {download_speed}down/{upload_speed}up, when I pay for {GUARANTEED_DOWNLOAD}down/{GUARANTEED_UPLOAD}up."

driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(message)
time.sleep(2)

# post button:
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()

print("Tweet posted🥳!!")