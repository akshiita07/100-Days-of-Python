from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# KEEP BROWSER OPEN:
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# CREATE DRIVER:
driver=webdriver.Chrome(options=chrome_options)

# URL OF Game PAGE:
driver.get("https://orteil.dashnet.org/experiments/cookie/")


five_seconds_timer = time.time() + 5   # 5 secs from now
five_minutes_timer = time.time() + 60*5   # 5 minutes from now
cookie=driver.find_element(By.ID,"cookie")

upgrade_item_id=[]
upgrades_list=driver.find_elements(By.CSS_SELECTOR,"#store div")
for upgrade in upgrades_list:
    # print(upgrade.get_attribute("id"))
    item_id=upgrade.get_attribute("id")
    upgrade_item_id.append(item_id)

while True:
    # click on the cookie:
    cookie.click()
        
    # Every 5 seconds: check right-hand pane to see which upgrades are affordable and purchase the most expensive one
    if time.time() > five_seconds_timer:
        
        upgrades_list=driver.find_elements(By.CSS_SELECTOR,"#store b")
        upgrade_prices=[]
        
        for upgrade in upgrades_list:
            # print(upgrade.text)
            text=upgrade.text
            if text!="":
                # split by 1
                # strip to remove spaces
                # remove , in cost
                cost=int(text.split("-")[1].strip().replace(",",""))
                upgrade_prices.append(cost)
                
        # create a dictionary {id:cost}
        cookie_upgrades={}
        for i in range(len(upgrade_prices)):
            # {cost,id}
            cookie_upgrades[upgrade_prices[i]]=upgrade_item_id[i]
        
        # COOKIE COUNT:
        current_cookie_count=driver.find_element(By.ID,"money").text
        if "," in current_cookie_count:
            # replace ,
            current_cookie_count=current_cookie_count.replace(",","")
        current_cookie_count=int(current_cookie_count)  #convert to int
        
        # FIND AFFORDABLE UPGRADES & BUY MOST EXENSIVE ONE:
        affordable_upgrades={}
        for cost,id in cookie_upgrades.items():
            if current_cookie_count>cost:
                # can buy:
                affordable_upgrades[cost]=id
        
        # find max:
        expensive_upgrade=max(affordable_upgrades)
        print(f"We are buying most expensive affordable upgrade of price: {expensive_upgrade}")
        expensive_upgrade_id=affordable_upgrades[expensive_upgrade]

        # click on this id:
        driver.find_element(By.ID,expensive_upgrade_id).click()
        
        # update time:
        five_seconds_timer=time.time()+5
        
            
    # After 5 min have passed since starting the game:stop bot and print "cookies/second"
    if time.time() > five_minutes_timer:
        cookies_per_second=driver.find_element(By.ID,"cps").text
        print(f"cookies/second= {cookies_per_second}")
        break

# driver.quit()