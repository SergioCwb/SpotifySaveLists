This script save a list in your Spotify using the Spotipy library.
Set and venv environment and install all the required libraries.
More info on https://github.com/techmatlock/spotify-discover-weekly-save-headless

The auth.py file must contain your Spotify credentials.

Adjust this two variables in the auth.py file:


<code>CLIENT_ID = '&lt;enter your client id here&gt;'
CLIENT_SECRET = '&lt;enter your client secret here&gt;'</code>
  
Also, you have to enter two playlists IDs in main.py:

<code>DISCOVER_WEEKLY_ID = '&lt;enter the Weekly Discover Playlist id here&gt;' 
SAVE_TO_ID = '&lt;enter the newly created Playlist id here - must exist&gt;'</code>

At the first access, spotify will ask for a token.
It will create an URL that you must access, and copy/paste the result URL with the token.
Copy the token and update it in main.py:

<code>REFRESH_TOKEN = '&lt;enter this very large token string here&gt;'</code>
