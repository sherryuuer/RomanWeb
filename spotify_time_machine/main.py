from spotify_client_keys import client_id, client_secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secrets,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
time_machine = input("Which year do you want to travel to ? Type YYYY-MM-DD: ")
year = time_machine.split("-")[0]


def get_song_list():
    import requests
    from bs4 import BeautifulSoup

    bb_url = f"https://www.billboard.com/charts/hot-100/{time_machine}/"

    response = requests.get(url=bb_url)
    bb_webpages = response.text
    soup = BeautifulSoup(bb_webpages, "html.parser")
    titles = soup.select("li ul li h3")
    titles = [x.getText().strip() for x in titles]
    return titles


# Function to get Spotify track URI from a song name
def get_track_uri(song_name):
    results = sp.search(q=f"track:{song_name} year:{year}", type='track')
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    else:
        pass


# Create a list of Spotify track URIs from the song names
song_names = get_song_list()
spotify_uris = [get_track_uri(song_name) for song_name in song_names]
playlist = sp.user_playlist_create(user=user_id, name=f"songs of {time_machine} created by sally's python code", public=False)

for song in spotify_uris:
    try:
        sp.playlist_add_items(playlist_id=playlist["id"], items=[song, ])
    except Exception as e:
        print(e)
        pass
print("New playlist successfully created on Spotify!")
