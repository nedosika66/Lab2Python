class Artist:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year
        self.tracks = []
        self.featured_tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def add_featured_track(self, track):
        self.featured_tracks.append(track)

    def summary(self):
        return f"Artist: {self.name}, Country: {self.country}, Tracks: {len(self.tracks)}"
