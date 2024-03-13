import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Spotipy with your client ID and client secret
client_credentials_manager = SpotifyClientCredentials(client_id='a14ddcfc23d1420f945b1965b124fac6', client_secret='df6d3ee9d5dc489f97305a3bc259700e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def main():
    print("Yo")

# Gets the details of the playlist and returns the track name and artist name in the form of a dictionary
def get_dict(id):
    playlist = sp.playlist(id)
    temp_dict = {}
    for track in playlist['tracks']['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        temp_dict[track_name] = artist_name
    return temp_dict

# print(get_dict("https://open.spotify.com/playlist/73Pb0ylLKE6BQjun5r0iCf"))

if __name__ == "__main__":
    main()