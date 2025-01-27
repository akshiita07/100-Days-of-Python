# INTERACT WITH WIKIPEDIA WEB PAGE
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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# GET TOTAL NO OF ARTICLES:
no_of_articles=driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
print(f"Total no of articles are: {no_of_articles.text}")

# CLICK ON TOTAL NO OF ARTICLES:
# no_of_articles.click()

# USING LINK_TEXT:
# news=driver.find_element(By.LINK_TEXT,"Wikinews").click()

# TYPE INTO INPUT FIELDS (full screen)
input_element=driver.find_element(By.NAME,"search")
# print(input_element)
input_element.send_keys("Python",Keys.ENTER)

# driver.quit()