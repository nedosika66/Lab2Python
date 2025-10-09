class Track:
    def __init__(self, title, duration, artist, bpm, key):
        self.__title = title
        self.__duration = duration
        self.artist = artist
        self.bpm = bpm
        self.key = key

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration):
        if new_duration > 0:
            self.__duration = new_duration

    def describe(self):
        print(f"{self.title} | Виконавець: {self.artist} | BPM: {self.bpm} | Key: {self.key} | Тривалість: {self.duration} хв")

    def analyze_mood(self):
        mood = "Сумний" if self.key.lower().endswith('m') else "Не сумний"
        return f"{self.title} — {mood} (тональність {self.key})"

    @staticmethod
    def compare_bpm(track1, track2):
        if track1.bpm > track2.bpm:
            return f"{track1.title} має швидший темп, ніж {track2.title}"
        elif track1.bpm < track2.bpm:
            return f"{track2.title} має швидший темп, ніж {track1.title}"
        else:
            return f"{track1.title} і {track2.title} мають однаковий BPM"


class RemixTrack(Track):
    def __init__(self, title, duration, artist, bpm, key, dj_name):
        super().__init__(title, duration, artist, bpm, key)
        self.dj_name = dj_name

    def describe(self):
        print(f"{self.title} (Remix) | Виконавець: {self.artist} | Ft: {self.dj_name} | BPM: {self.bpm} | Key: {self.key} | Тривалість: {self.duration} хв")


class ReleaseInfo:
    def __init__(self, release_name, year, label):
        self.release_name = release_name
        self.year = year
        self.label = label


class AlbumTrack(Track, ReleaseInfo):
    def __init__(self, title, duration, artist, bpm, key, track_number, is_single, release_name, year, label):
        Track.__init__(self, title, duration, artist, bpm, key)
        ReleaseInfo.__init__(self, release_name, year, label)
        self.track_number = track_number
        self.is_single = is_single

    def describe(self):
        single_info = "Сингл" if self.is_single else f"Трек №{self.track_number} альбому"
        print(f"{self.title} | Виконавець: {self.artist} | BPM: {self.bpm} | Key: {self.key} | {single_info} | Альбом: {self.release_name} ({self.year}, {self.label}) | Тривалість: {self.duration} хв")

    def publish_report(self):
        return f"Трек '{self.title}' випущено як частину альбому '{self.release_name}' ({self.year}) на лейблі {self.label}"


if __name__ == "__main__":
    track1 = Track("The Light", 2.52, "Juice WRLD", 170, "A#m")
    track2 = Track("Best Friend", 3.33, "Young Thug", 127, "A")
    remix1 = RemixTrack("Lucid Dreams", 4.12, "Juice WRLD", 84, "F#m", "Lil uzi vert")
    album_track = AlbumTrack("Wish", 2.56, "Trippie redd", 94, "A", 3, False, "LIFE`S A TRIP", 2018, "TenThousand Projects")

    print("\n=== Сингли ===")
    track1.describe()
    print(track1.analyze_mood())
    print("-" * 80)
    track2.describe()
    print(track2.analyze_mood())
    print("-" * 80)

    print("\n=== Ремікс ===")
    remix1.describe()
    print(remix1.analyze_mood())
    print("-" * 80)

    print("\n=== Трек з альбому ===")
    album_track.describe()
    print(album_track.publish_report())
    print(album_track.analyze_mood())
    print("-" * 80)

    print("\n=== Плейлист ===")
    playlist = [track1, track2, remix1, album_track]
    for track in playlist:
        track.describe()
    print("-" * 80)

    print("\n=== Порівняння темпу ===")
    print(Track.compare_bpm(track1, track2))
    print(Track.compare_bpm(remix1, album_track))
    print("-" * 80)

    print("\n=== Інші версії ===")
    track1.title = "Lucid Dreams (Acoustic Version)"
    track1.duration = 3.51
    track1.describe()
    print("-" * 80)
