#!/usr/bin/env python3

from src.clients import GeniusAPIClient
from src.services import LyricsService
from src.utils import config, FileHandler


def main() -> None:

    # Ge the .env and searches.txt file.
    if not config.validate():
        print("\n Tip: Create a .env file with GENIUS_ACCESS_TOKEN=your_token")
        return
    
    searches = FileHandler.load_searches(config.SEARCHES_FILE)
    
    if not searches:
        print(f" Error: No searches found in '{config.SEARCHES_FILE}'")
        print(f" Tip: Create '{config.SEARCHES_FILE}' with one search per line")
        return
    
    print(f"\n{'='*60}")
    print(f"🎵 Lyrics Eater - Processing {len(searches)} searches")
    print(f"{'='*60}\n")
    
    # Search songs and extract the lyrics
    genius_client = GeniusAPIClient(config.GENIUS_ACCESS_TOKEN)
    lyrics_service = LyricsService(genius_client)
    
    songs, successful, failed = lyrics_service.process_multiple_queries(searches)
    
    if songs:
        print(f"\n{'='*60}")
        print(" Saving results...")
        FileHandler.save_to_excel(songs, config.OUTPUT_FILE)
        
        print(f"\n Process completed!")
        print(f"    Successful: {successful}/{len(searches)}")
        print(f"    Failed: {failed}/{len(searches)}")
        print(f"    Output: {config.OUTPUT_FILE}")
    else:
        print("\n No songs were successfully processed")


if __name__ == "__main__":
    main()
