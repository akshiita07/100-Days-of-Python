import requests
from twilio.rest import Client
import os
import random
from dotenv import load_dotenv
load_dotenv("Day36_Stock_Trading_News_Alert_Project/.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# https://www.alphavantage.co
alphavantage_api_key=os.getenv("API_KEY")
#https://newsapi.org/docs/endpoints/everything
news_api_key=os.getenv("NEWS_API_KEY")

# from twilio:
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

# print(f"API_KEY: {alphavantage_api_key}")
# print(f"news_api_key: {news_api_key}")
# print(f"AUTH_TOKEN: {auth_token}")
# print(f"AUTH_SID: {account_sid}")

parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":alphavantage_api_key,
}

parameters_news={
    "q":COMPANY_NAME,
    "apikey":news_api_key,
}

response=requests.get(url="https://www.alphavantage.co/query",params=parameters)
response_news=requests.get(url="https://newsapi.org/v2/everything",params=parameters_news)
# print(f"Status code is: {response.status_code}")
response.raise_for_status()
response_news.raise_for_status()
stock_data=response.json()
news_data=response_news.json()
# print(stock_data)   # json viewer: https://jsonviewer.stack.hu/
# print(news_data) 


# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def sendMessage(has_drop,rate,random_news):
    client = Client(account_sid, auth_token)
    arrow="🔺"
    if has_drop==True:
        arrow="🔻"
        
    news_title=random_news["title"]
    news_desc=random_news["description"]
    
    # send WHATSAPP TEXT:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"{STOCK}: {arrow}{rate}%\nHeadline: {news_title}\nBrief: {news_desc}\n",
        to='whatsapp:+918283840233'       
    )

    # print(message.sid)
    
# fetch the first 3 articles for the COMPANY_NAME. 
news=news_data["articles"]
three_news=news[:3]
random_news=random.choice(three_news)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News"):
stock_daily=stock_data["Time Series (Daily)"]
daily_list=[value for (key,value) in stock_daily.items()]   #dictionary comprehension
yesterday_close=float(daily_list[0]["4. close"])
day_before_yesterday_close=float(daily_list[1]["4. close"])
# print(f"Yest: {yesterday_close}")
# print(f"Day before Yest: {day_before_yesterday_close}")
has_drop=False      #variable to keep track of inc/dec
rate=(yesterday_close-day_before_yesterday_close)/yesterday_close
if (rate)<0:
    has_drop=True
if abs(rate*100) >0.05:
    print("Get News")
    sendMessage(has_drop,abs(rate),random_news)
    
    
    