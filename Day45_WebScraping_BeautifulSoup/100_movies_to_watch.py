import requests
from bs4 import BeautifulSoup

response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data=response.text

soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())

movies=[]
movie_link=soup.select(".article-title-description__text  .title")
for m in movie_link:
    movies.append(m.getText())

print("List of movies:")
movies.reverse()
print(movies)

with open("./Day45_WebScraping_BeautifulSoup/moviesList.txt",mode="w",encoding="utf-8") as file:
    for m in movies:
        file.write(f"{m}\n")
    