from track import Track

class FeatureTrack(Track):
    def __init__(self, title, artist, bpm, key_signature, structure, genre, featured_artist):
        super().__init__(title, artist, bpm, key_signature, structure, genre)
        self.featured_artist = featured_artist
        self.featured_artist.add_featured_track(self)

    def summary(self):
        return f"{super().summary()} | Feat: {self.featured_artist.name}"
