import requests
from bs4 import BeautifulSoup


class TrackInfo:
    """
    An object containing track information and operations necessary for
    scraping the info off of 1001tracklists.com
    """


    def __init__(self, url):
        self.url = url
        self.tracklist_id = self.url.split('tracklist/')[1].split('/')[0] # Get id from url

        self.tracks = []
        self.track_names = []
        self.artist_names = []
        self.spotify_links = []
        self._soup = self._get_soup()
        self._track_soup = self._soup.find_all("div", class_="fontL")
        self.fill_info()


    def _get_soup(self):
        """Get HTML soup of current webpage"""
        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def get_tracklist_title(self):
        """Scrapes the webpage for the tracklist title"""
        title = self._soup.find("h1", id="pageTitle")
        return(title.text)
    
    def fill_info(self):
        """Fill class arrays with all links, artist, and track on the page""" 

        print(f"Generating data for{self.get_tracklist_title()}")

        for tracks in self._track_soup:
            track = tracks.find("meta", itemprop="name")['content']
            self.tracks.append(track)
            split = track.split(' - ')
            track_name, artist_name = split[1], split[0]
            self.track_names.append(track_name)
            self.artist_names.append(artist_name)

def main():
    track = TrackInfo("https://www.1001tracklists.com/tracklist/9l2wdv1/two-friends-big-bootie-mix-018-2020-10-26.html")
    for song in track.tracks:
        print(song)
    


if __name__ == "__main__":
    main()