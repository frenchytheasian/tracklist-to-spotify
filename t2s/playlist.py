import sys

from trackinfo import TrackInfo

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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
    tracks = ti.tracks

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    userID = "test"
    playlist = sp.user_playlist_create(userID, ti.get_tracklist_title())
    l = []

    for track in tracks:
        search = sp.search(q=track,limit=1)
        uri = search['tracks']['items'][0]['uri']
        track = sp.track(uri)
        l.append(track)

    sp.user_playlist_add_tracks(userID, playlist.id, l)

if __name__ == '__main__':
    create_playlist()