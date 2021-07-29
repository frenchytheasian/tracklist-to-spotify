from trackinfo import TrackInfo

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
    

def main():
    track = TrackInfo('https://www.1001tracklists.com/tracklist/9l2wdv1/two-friends-big-bootie-mix-018-2020-10-26.html')
    print(track)
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    artist = sp.artist('spotify:artist:3jOstUTkEu2JkjvRdBA5Gu')
    print(artist)

if __name__ == '__main__':
    main()