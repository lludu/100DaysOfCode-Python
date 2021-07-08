
#------------------- Import Modules --------------------#
from bs4 import BeautifulSoup
# Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from p_data import *
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
# Spotipy Documentation: https://spotipy.readthedocs.io/en/2.18.0/


# ----- Inspect Webpage to identify Song Title Tags ----- #
# -- Song Name CSS Class: chart-element__information__song --#
# -- Song Artist CSS Class: chart-element__information__artist --#
# -- Song Rank Number CSS Class: chart-element__rank__number --#

# -- Test for first result -- #
# rank = soup.find(name="span", class_="chart-element__rank__number").getText()
# print(rank)
# name = soup.find(name="span", class_="chart-element__information__song").getText()
# print(name)
# artist = soup.find(name="span", class_="chart-element__information__artist").getText()
# print(artist)




# #------------------- Get the date for the time machine and create the url for beautifulsoup --------------------#
date_input = input("What date do you want to travel back to? Type the date in this format: YYYY-MM-DD: ")
billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
time_machine_url = billboard_endpoint + date_input

# #------------------- Scrape the data (song titles) from the requested time_machine_url --------------------#
response = requests.get(time_machine_url)
contents = response.text

# #------------------- Change contents to soup --------------------#
soup = BeautifulSoup(contents, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song")
songs = [song.getText() for song in all_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{date_input[:4]}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
#print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)