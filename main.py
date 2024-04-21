import requests
import base64
import json
import os
from auth import *

REFRESH_TOKEN = '<enter the token string here>'
DISCOVER_WEEKLY_ID = '<enter the Weekly Discover Playlist id here>' 
SAVE_TO_ID = '<enter the newly created Playlist id here - must exist>'

# save from the Weekly Discover Playlist from Spotify
#   https://open.spotify.com/playlist/<enter the playlist ID here>
# to
# Your playlist here
#   https://open.spotify.com/playlist/<your playlist id here>

OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
def refresh_access_token():
    payload = {
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
    }
    encoded_client = base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode('ascii'))
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic %s" % encoded_client.decode('ascii')
    }
    response = requests.post(OAUTH_TOKEN_URL, data=payload, headers=headers)
    return response.json()


def get_playlist(access_token):
    url = "https://api.spotify.com/v1/playlists/%s" % DISCOVER_WEEKLY_ID
    headers = {
       "Content-Type": "application/json",
       "Authorization": "Bearer %s" % access_token
    }
    response = requests.get(url, headers=headers)
    return response.json()

def add_to_playlist(access_token, tracklist):
    url = "https://api.spotify.com/v1/playlists/%s/tracks" % SAVE_TO_ID
    payload = {
        "uris" : tracklist
    }
    headers = {
       "Content-Type": "application/json",
       "Authorization": "Bearer %s" % access_token
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()


def main():
    if REFRESH_TOKEN is None or CLIENT_ID is None or CLIENT_SECRET is None or DISCOVER_WEEKLY_ID is None or SAVE_TO_ID is None:
        print("Environment variables have not been loaded!")
        return

    access_token = refresh_access_token()['access_token']
    tracks =  get_playlist(access_token)['tracks']['items']
    tracklist = []
    for item in tracks:
        print('Adding track ' + str(item['track']['name']))
        tracklist.append(item['track']['uri'])
    response = add_to_playlist(access_token, tracklist)

    if "snapshot_id" in response:
        print("Successfully added all songs")
    else:
        print(response)

main()