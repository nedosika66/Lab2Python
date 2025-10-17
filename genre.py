class Genre:
    def __init__(self, name, year_created):
        self.name = name
        self.year_created = year_created
        self.tracks = []

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)

    def summary(self):
        return f"Genre: {self.name}, Tracks: {len(self.tracks)}"

    def average_bpm(self):
        if not self.tracks:
            return 0
        return sum(t.bpm for t in self.tracks) / len(self.tracks)
