from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv("Day47_Amazon_Price_Tracker/.env")

# SET A TARGET PRICE:
target_price=100

# WEB SCRAPING TO GET INTEGER PRICE:
# all headers available at: https://httpbin.org/headers and https://myhttpheader.com/
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}
response=requests.get(url="https://appbrewery.github.io/instant_pot/",headers=header)    #trial website
# response=requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=header)       #actual website
data=response.text
soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())
tag1=soup.find(name="span",class_="a-price-whole")
price_tag=tag1.getText()
price_tag=price_tag.split(".")[0]
print(f"Price tag is: {price_tag}")
tag2=soup.find(name="span",id="productTitle")
product_name=tag2.getText()
print(f"Product name is: {product_name}")
link_to_buy="https://appbrewery.github.io/instant_pot/"

# SEND MAIL WHEN PRICE IS BELOW OUR SET PRICE:
if int(price_tag)<target_price:
    my_email="apathak1_be22@thapar.edu"
    password=os.getenv("EMAIL_PASSWORD")
    msg=f"Subject: From Python Day 47\n\nThe price of your desired product {product_name} is now {price_tag} below your desired price. Buy Now!! {link_to_buy}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pathakshita07@gmail.com",
            msg=msg.encode("utf-8")
        )
    print("Email sent!🥳")