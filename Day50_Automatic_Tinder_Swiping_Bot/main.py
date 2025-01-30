from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found
import os
import time
from dotenv import load_dotenv

# env file:
load_dotenv("Day50_Automatic_Tinder_Swiping_Bot/.env")
email_id=os.getenv("EMAIL")
password=os.getenv("PASSWORD")
# print(f"Email: {email_id}")

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF tinder page:
driver.get("https://tinder.com/app/recs")
time.sleep(3)

# accept t&c:
driver.find_element(By.CSS_SELECTOR,"#u1469300313 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\$c-ds-background-primary\).C\(\$c-ds-text-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(1) > button > div.w1u9t036 > div.c9iqosj").click()
time.sleep(1)

# log in:
driver.find_element(By.XPATH,'//*[@id="u1469300313"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()
time.sleep(6)

# sign in with facebook:
# if directly fb sign-in btn is not found then first click on other options:

try:
    driver.find_element(By.XPATH,'//*[@id="u1690640749"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
except NoSuchElementException:
    driver.find_element(By.XPATH,'//*[@id="u1690640749"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button').click()
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="u1690640749"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
time.sleep(5)

base_window = driver.current_window_handle
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# email:
driver.find_element(By.NAME,"email").click()
driver.find_element(By.NAME,"email").send_keys(email_id,Keys.TAB)
time.sleep(1)

# password:
driver.find_element(By.NAME,"pass").click()
driver.find_element(By.NAME,"pass").send_keys(password,Keys.ENTER)
time.sleep(5)

print(f"AFter password i am at: {driver.title}")

# continue:
try:
    driver.find_element(By.XPATH,'//*[@id="mount_0_0_jE"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]').click()
except NoSuchElementException:
    print("Could not find that continue btn")
    print(f"Still at: {driver.title}")
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="mount_0_0_jE"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]').click()

time.sleep(5)
driver.switch_to.window(base_window)
print(driver.title)

# allow location:
driver.find_element(By.XPATH,'//*[@id="u1690640749"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(1)

# do NOT allow notifications:
driver.find_element(By.XPATH,'//*[@id="u1690640749"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]').click()
time.sleep(1)

# no swipe:
try:
    driver.find_element(By.XPATH,'//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[2]/button').click()
    time.sleep(1)
except NoSuchElementException:
    time.sleep(5)       #try again after 5s