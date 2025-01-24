from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://news.ycombinator.com/news")
# print(response.text)  

soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

articles=soup.select(".titleline")
texts=[]
links=[]
votes=[]

for item in articles:
    texts.append(item.find("a").getText())
    links.append(item.find("a").get("href"))
    
upVotes=soup.find_all(name="span",class_="score") 
for item in upVotes:
    votes.append(item.getText())

print("\nHeadings:")
print(texts)

print("\nLinks:")
print(links)

# print("\nVotes:")
# print(votes)

# get integer out of votes:
integer_votes=[]
for vote in votes:
    integer_votes.append(int(vote.split()[0]))
print("\nUpdated Votes:")
print(integer_votes)

# get maximum upvote count:
# maxi=integer_votes[0]
# for i in range(1,len(integer_votes)):
#     if integer_votes[i]>maxi:
#         maxi=integer_votes[i]
#         ind=i

maxi=max(integer_votes)
ind=integer_votes.index(maxi)
print(f"Max upvote: {maxi} and index: {ind}")
print(f"Title of story with maximum upvotes= {texts[ind]} and link is {links[ind]}")