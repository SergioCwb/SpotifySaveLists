This script save a list in your Spotify using the Spotipy library.
Set and venv environment and install all the required libraries.
More info on https://github.com/techmatlock/spotify-discover-weekly-save-headless

The auth.py file must contain your Spotify credentials.

Adjust this two variables in the auth.py file:

CLIENT_ID = '<enter your client id here>'
CLIENT_SECRET = '<enter your client secret here>'

Also, you have to enter two playlists IDs in main.py:

DISCOVER_WEEKLY_ID = '<enter the Weekly Discover Playlist id here>' 
SAVE_TO_ID = '<enter the newly created Playlist id here - must exist>'

At the first access, spotify will ask for a token.
It will create an URL that you must access, and copy/paste the result URL with the token.
Copy the token and update it in main.py:

REFRESH_TOKEN = '<enter this very large token string here>'
