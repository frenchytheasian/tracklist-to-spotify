import sys

from trackinfo import TrackInfo

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
    

def main():
    """
    Create a spotify playlist from a tracklist. Use the scraped info 
    gathered by the TrackInfo object

    """
    tracklist_url = sys.argv[1]

    tracks = TrackInfo(tracklist_url).tracks

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    search = sp.search(q=tracks[0], limit=1)

    #TODO: figure out how to create a playlist using the spotipy library
    uri = search['tracks']['items'][0]['uri']
    print(uri)
    track = sp.track(uri)

    # TODO: move the prior couple of lines into this for loop
    # for track in tracks:
    #     search = sp.search(q=track,limit=1)
    #     print(search['tracks'].keys())


if __name__ == '__main__':
    main()