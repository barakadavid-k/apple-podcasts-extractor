thonimport json

class DataExporter:
    def export_to_json(self, data, file_name='podcast_data.json'):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)