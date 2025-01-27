# SENDING KEYS
from selenium import webdriver
from selenium.webdriver.common.by import By
# keys:
from selenium.webdriver.common.keys import Keys

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF WIKIPEDIA MAIN PAGE:
driver.get("http://secure-retreat-92358.herokuapp.com/")

# TYPE INTO INPUT FIELDS (full screen)
input_fname=driver.find_element(By.NAME,"fName")
input_lname=driver.find_element(By.NAME,"lName")
input_email=driver.find_element(By.NAME,"email")

input_fname.send_keys("Akshita",Keys.TAB)
input_lname.send_keys("Pathak",Keys.TAB)
input_email.send_keys("pathakshita07@gmail.com",Keys.ENTER)
print("Done")

# driver.quit() 