thonimport sys
import logging
from extractors.podcast_parser import PodcastParser
from outputs.exporters import DataExporter

def main():
    logging.basicConfig(level=logging.INFO)
    
    podcast_url = sys.argv[1] if len(sys.argv) > 1 else None
    if not podcast_url:
        logging.error("No podcast URL provided!")
        sys.exit(1)

    logging.info(f"Starting extraction for podcast: {podcast_url}")

    parser = PodcastParser(podcast_url)
    podcast_data = parser.extract_podcast_data()

    if not podcast_data:
        logging.error("Failed to extract podcast data!")
        sys.exit(1)

    logging.info("Exporting extracted data...")
    exporter = DataExporter()
    exporter.export_to_json(podcast_data)
    logging.info("Data export completed.")

if __name__ == "__main__":
    main()