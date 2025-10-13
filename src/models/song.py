"""Song data model. """

from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    """
    Represents a song with its metadata and lyrics.
    
    """
    
    song_id: int
    title: str
    artist: str
    url: str
    genres: str = "N/A"
    label: str = "N/A"
    album: str = "N/A"
    release_date: str = "N/A"
    lyrics: str = "N/A"
    
    def to_dict(self) -> dict:
        """
        Convert Song to dictionary for DataFrame/Excel export.
        
        """
        return {
            'genero': self.genres,
            'artista': self.artist,
            'cancion': self.title,
            'letras': self.lyrics,
            'enlace_genius': self.url,
            'discografica': self.label
        }
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.title} - {self.artist}"
