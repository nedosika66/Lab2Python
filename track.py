from genre import Genre
from artist import Artist

class Track:
    all_tracks = []

    def __init__(self, title: str, artist: Artist, bpm: int, key_signature: str, structure: str, genre: Genre):
        self.title = title
        self._artist = artist
        self.bpm = bpm
        self.key_signature = key_signature
        self.structure = structure
        self._genre = genre
        artist.add_track(self)
        genre.add_track(self)
        Track.all_tracks.append(self)

    def summary(self):
        return f"{self.title} | Artist: {self._artist.name} | BPM: {self.bpm} | Key: {self.key_signature} | Genre: {self._genre.name}"

    def change_bpm(self, new_bpm: int):
        old_bpm = self.bpm
        self.bpm = new_bpm
        print(f"\nBPM for '{self.title}' changed from {old_bpm} to {self.bpm}")

    @staticmethod
    def bpm_to_seconds(bpm: int) -> float:
        return 60 / bpm

    def is_sad(self) -> bool:
        return "minor" in self.key_signature.lower()

    @property
    def artist(self):
        return self._artist

    @property
    def genre(self):
        return self._genre
