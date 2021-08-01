import sys

from trackinfo import TrackInfo

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# TODO: Maybe create the functionality to create a bunch of playlist from a 
# list of tracklists. This probably isn't practical though, because no one 
# probably needs to create many playlists at once.

def create_playlist():
    """
    Create a spotify playlist from a tracklist. Use the scraped info 
    gathered by the TrackInfo object

    """
    tracklist_url = sys.argv[1]

    ti = TrackInfo(tracklist_url)
    scope = "playlist-modify-private playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlist = sp.user_playlist_create('michael.x.french', ti.get_tracklist_title())
    songs_to_add = []
    tracks = ti.tracks
    count = 0

    for track in tracks:
        search = sp.search(q=track,limit=1)
        track_json = search['tracks']['items']

        if track_json:
            # Sometimes the search is turning up empty
            uri = track_json[0]['uri']
            songs_to_add.append(uri)

        if len(songs_to_add) == 100:
            sp.playlist_add_items(playlist['id'], songs_to_add)
            songs_to_add = []

        print(f"{count}\{len(tracks)}")
        count += 1
    
    sp.playlist_add_items(playlist['id'], songs_to_add)

if __name__ == '__main__':
    create_playlist()