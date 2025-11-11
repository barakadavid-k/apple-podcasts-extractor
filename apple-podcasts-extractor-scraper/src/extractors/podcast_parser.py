thonimport requests
from bs4 import BeautifulSoup

class PodcastParser:
    def __init__(self, podcast_url):
        self.podcast_url = podcast_url

    def extract_podcast_data(self):
        try:
            response = requests.get(self.podcast_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            podcast_data = {
                'podcast_name': self._get_podcast_name(soup),
                'artist_name': self._get_artist_name(soup),
                'description': self._get_description(soup),
                'categories': self._get_categories(soup),
                'artwork': self._get_artwork_url(soup),
                'release_date': self._get_release_date(soup),
            }

            return podcast_data
        except requests.RequestException as e:
            print(f"Error fetching podcast data: {e}")
            return None

    def _get_podcast_name(self, soup):
        return soup.find('h1', class_='podcast-name').get_text()

    def _get_artist_name(self, soup):
        return soup.find('h2', class_='artist-name').get_text()

    def _get_description(self, soup):
        return soup.find('meta', {'name': 'description'})['content']

    def _get_categories(self, soup):
        categories = []
        category_tags = soup.find_all('span', class_='category')
        for category in category_tags:
            categories.append({'id': category['data-id'], 'name': category.get_text()})
        return categories

    def _get_artwork_url(self, soup):
        return soup.find('img', class_='podcast-artwork')['src']

    def _get_release_date(self, soup):
        return soup.find('time', class_='release-date').get_text()