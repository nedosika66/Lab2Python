from track import Track

class TrackWithLyrics(Track):
    def __init__(self, title, artist, bpm, key_signature, structure, genre, lyricist, lyrics):
        super().__init__(title, artist, bpm, key_signature, structure, genre)
        self.lyricist = lyricist
        self.lyrics = lyrics

    def summary(self):
        return f"{super().summary()} | Lyricist: {self.lyricist} | Words: {len(self.lyrics.split())}"

    def word_count(self):
        return len(self.lyrics.split())
