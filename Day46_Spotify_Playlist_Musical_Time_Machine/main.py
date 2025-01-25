import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import time

# env:
load_dotenv("Day46_Spotify_Playlist_Musical_Time_Machine/.env")
spotify_api_key=os.getenv("CLIENT_ID")
spotify_api_secret=os.getenv("CLIENT_SECRET")

# 3. USE SPOTIFY API TO CREATE A NEW PLAYLIST FOR THAT YEAR
# https://developer.spotify.com/dashboard

# authenticate your Python project with Spotify using your unique Client ID/ Client Secret
# pip install spotipy
# playlist-modify-public scope to create a new public playlist & add items to it
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_api_key,
                                               client_secret=spotify_api_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public"
                                               )
                    )

# Get the user id of the authenticated user (your Spotify username).
# print(sp.current_user())
print(f"Your spotify display name is {sp.current_user()['display_name']}")
print(f"Your spotify display name is {sp.current_user()['id']}")

date=input("What year you would like to travel to in YYYY-MM-DD format: ")   #2020-01-01
# 1. USE BEAUTIFUL SOUP TO SCRAPE TOP 100 SONGS FROM A PARTICULAR YEAR
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response=requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/",headers=header)
content=response.text
# print(content)

soup=BeautifulSoup(content,"html.parser")
# print(soup.prettify())

# 2. EXTRACT SONG TITLES FROM LIST
link=soup.select("li ul li h3")
song_titles=[]
for item in link:
    song_titles.append(item.getText().strip())
# print("List of song titles: ")
# print(song_titles)

# 4. SEARCH SPOTIFY FOR EACH SONG & ADD THOSE SONGS TO THIS PLAYLIST
song_urls=[]
# extract year from the date
year=date.split("-")[0]
for song in song_titles:
    response=sp.search(q=f"track:{song} year:{year}", type="track")
    time.sleep(1)
    # pprint(repsonse.text)
    
    try:
        song_urls.append(response["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print("List of song urls: ")
# print(song_urls)

# CREATE NEW SPOTIFY PLAYLIST:
playlist=sp.user_playlist_create(sp.current_user()["id"], f"{date} Billboard 100", public=True, collaborative=False, description="Python dat 46 project")
# ADD SONGS FROM song_urls TO THIS NEW PLAYLIST
sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
print("Playlist created!")