thonimport json

class DataExporter:
    def __init__(self):
        pass

    def export(self, podcast_data, episode_data):
        with open('output.json', 'w') as outfile:
            json.dump({
                'podcasts': podcast_data['results'],
                'episodes': episode_data
            }, outfile, indent=4)