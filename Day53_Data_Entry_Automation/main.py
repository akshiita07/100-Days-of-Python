# address
# price
# link of property
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException # custom exception when an element cannot be found

# constants:
ZWILLOW_URL="https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL="https://forms.gle/vC1VihYkebEZSTnNA"

# WEB SCRAPE SITE USING BEAUTIFUL SOUP
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response=requests.get(url=ZWILLOW_URL,headers=header)
soup=BeautifulSoup(response.text,"html.parser")

prices=[]
address=[]
links=[]

# loop over all:
for item in soup.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper"):
    zillow_data_price_tag=item.find(name="span",class_="PropertyCardWrapper__StyledPriceLine")
    # print(zillow_data_price_tag.getText())
    zillow_data_price_tag=zillow_data_price_tag.getText()
    zillow_data_price_tag=zillow_data_price_tag.split("+")[0]
    zillow_data_price_tag=zillow_data_price_tag.split("/")[0]
    # print(f"Price: {zillow_data_price_tag}")
    prices.append(zillow_data_price_tag)

    zillow_data_address_tag=item.find(name="address",attrs={"data-test": "property-card-addr"}).getText()
    zillow_data_address_tag=zillow_data_address_tag.strip()     #remove blank spaces from starting & ending
    zillow_data_address_tag=zillow_data_address_tag.split("|")[0]     #remove content after | character
    # print(f"Address: {zillow_data_address_tag}")
    address.append(zillow_data_address_tag)

    zillow_data_link_tag=item.find(name="a",attrs={"data-test": "property-card-link"}).get("href")
    # print(f"Link: {zillow_data_link_tag}")
    links.append(zillow_data_link_tag)


print("Prices list:")
print(prices)
print("\nAddresses list:")
print(address)
print("\nLinks list:")
print(links)

# FILL GOOGLE FORM USING SELENIUM
# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# FILL FORM FOR EACH ENTRY 
for i in range(len(prices)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)
    
    # fill address:
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address[i],Keys.TAB)
    
    
    # price:
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i],Keys.TAB)
    
    # link:
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
    
    # submit button:
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    
    time.sleep(2)

print("Added all in google forms.")

# show responses in google sheet:
# driver.get("https://docs.google.com/forms/d/1pf6gGmTUa1iAKP83d9kTifpv3lg8Sh-uXr7oG4igJ_M/edit#responses")
# driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]').click()