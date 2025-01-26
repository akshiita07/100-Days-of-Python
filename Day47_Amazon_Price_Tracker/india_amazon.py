from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv("Day47_Amazon_Price_Tracker/.env")

# SET A TARGET PRICE:
target_price=45000

# WEB SCRAPING TO GET INTEGER PRICE:
# all headers available at: https://httpbin.org/headers and https://myhttpheader.com/

# get COOKIES FROM DEVELOPER TOOLS->APPLICATION->STORAGE->COOKIES->AMAZON.IN & COPY VALUES INTO HEADER:
cookies={
    "csm-hit":"tb:0GNS16TCBX5592BNNBWW+s-CSKM13P5JDHB2978HP9S|1737871409681&t:1737871409681&adb:adblk_no",
    "i18n-prefs":"INR",
    "session-id":"144-5859977-9664403",
    "session-id-time":"2082787201l",
    "session-token":"YWeg89wgR249qpdNVz/E4LTJd2juVZiMY8BYaZ8m+i8uuFoq+XqCaXEMB3SS4uV7D+IHoL7EMRMDfMjhDQuqYbHsKoLtabe2IUCukHAQ+fjK3/sujCpHytzT2H1HkNlkjdtXNtJAxCCT2AWZYGldnun6VIRgB0YjQ2V3a4OtzxV/pomlxgkafDLsRqQ1YQsHIM5X/UfezR/dQsoUAjmDzYj5PdFQuov8l0C2LjKG7OE56Ter8K4yslmoEVJHT5n5nzHr2FXrIUHMfgDfo5KU0c+JHZcHiOphrHzHi/3XTfhETzRcjUXaCCFnSUFxfAiig82yKyy3rSdLIGkjIfqyJ+w6E5m6hTnCvrTQ4bOOb96XBeOSEkoAY+aXk9DXukWh",
    "ubid-acbin":"257-8141874-5347518"
}
header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}
URL_ENDPOINT="https://www.amazon.in/Dyson-Airwrap-Multi-Styler-Dryer-Vinca/dp/B0DNZDZFFP/ref=sr_1_2?crid=2OBCUEY055RHY&dib=eyJ2IjoiMSJ9.Vyx-9TK-oFvMm46ih4ZmqlnYqsJWiIeeJus1DIfN3CHxkVQ55DsBjL0uCWE2tG5gzd7z__qjlvB4wufGdjEquvufuXjR5zDnn3KNZmqpxY8d-UsH4Yc_D_RaKHf97Njp58StBdok4EVeX1c_XVUVzBQ4RCL3pbVeoTzxpqbRsNW9VJb_LPspgsw7kbeslPVQqtZYmT233BtWBNT1jEU9sk0a_KJTu811qhud3LHDzV8.-d5s72eKlc33vuyLdllRwrHn8gzP1q1WlfWStMaT9HI&dib_tag=se&keywords=dyson%2Bairwrap&nsdOptOutParam=true&qid=1737870544&sprefix=dyson%2Bair%2Bstra%2Cspecialty-aps%2C225&sr=8-2&th=1"
response=requests.get(url=URL_ENDPOINT,headers=header,cookies=cookies)
data=response.text
soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())
tag1=soup.find(name="span",class_="a-price-whole")
price_tag=tag1.getText()
price_tag=price_tag.split(".")[0]
price_tag_initial=price_tag.split(",")[0]
price_tag_after=price_tag.split(",")[1]
price_tag=f"{price_tag_initial}{price_tag_after}"
print(f"Price tag is: {price_tag}")
tag2=soup.find(name="span",id="productTitle")
product_name=tag2.getText()
print(f"Product name is: {product_name}")
link_to_buy=URL_ENDPOINT

# SEND MAIL WHEN PRICE IS BELOW OUR SET PRICE:
if int(price_tag)<target_price:
    my_email="apathak1_be22@thapar.edu"
    password=os.getenv("EMAIL_PASSWORD")
    msg=f"Subject: From Python Day 47\n\nThe price of your desired product {product_name} is now {price_tag} ie below your desired price. Buy Now!! {link_to_buy}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pathakshita07@gmail.com",
            msg=msg.encode("utf-8")
        )
    print("Email sent!🥳")