from artist import Artist
from genre import Genre
from track import Track
from feature_track import FeatureTrack
from track_with_lyrics import TrackWithLyrics

juice = Artist("Juice WRLD", "USA", 1998)
trippie = Artist("Trippie redd", "USA", 1999)
future = Artist("Future", "USA", 1983)
thug = Artist("Young Thug", "USA", 1991)
uzi = Artist("Lil Uzi Vert", "USA", 1994)

emo_rap = Genre("Emo Rap", 2010)
rage = Genre("Rage", 2017)
trap = Genre("Trap", 2000)
jersey_club = Genre("Jersey Club", 1990)

Track("In My Head", juice, 160, "F minor", "I-C-B-V-B-C-V-B-C", emo_rap)
Track("Hard To Choose One", future, 119, "B# major", "I-C-V-C-V-C-O", trap)
Track("Best Friend", thug, 127, "A major", "I-C-V-C-V-C", trap)
Track("Just Wanna Rock", uzi, 128, "B major", "I-C-V-C-O", jersey_club)
FeatureTrack("Matt Hardy 999", trippie, 79, "C# major", "I-V-V-V-V-V-V-V", rage, juice)
FeatureTrack("Wasted", juice, 145, "C major", "I-C-PC-V-C-PC-V-C-PC-V-C-O", emo_rap, uzi)
FeatureTrack("Money On Money", thug, 120, "A major", "I-C-V-C-V-C", trap, future)
TrackWithLyrics(
    "Lucid Dreams", juice, 84, "F# minor", "I-C-V-C-B-C-O", emo_rap, "Juice WRLD",
    "I still see your shadows in my room. Cant take back the love that I gave you. Its to the point where I love and I hate you. And I cannot change you, so I must replace you, oh"
)
TrackWithLyrics(
    "XO Tour Llif3", uzi, 155, "B minor", "V-C-PC-V-C-PC", emo_rap, "",
    "Days come and go, But my love gon' stay, Stay on the road, So my money straight. Uh oh you 'bout that? Uh uh you 'bout that?"
)

print("Songs:")
for track in Track.all_tracks:
    print(track.summary())

print("\nArtists:")
for artist in [juice, trippie, future, thug, uzi]:
    print(f"Artist: {artist.name}, Country: {artist.country}, Tracks: {len(artist.tracks)}")

print("\nGenres:")
for genre in [emo_rap, rage, trap, jersey_club]:
    print(f"Genre: {genre.name}, Year: {genre.year_created}, Tracks: {len(genre.tracks)}")


Track.all_tracks[0].change_bpm(80)
print(f"\nSeconds per beat at {Track.all_tracks[0].bpm} BPM: {Track.bpm_to_seconds(Track.all_tracks[0].bpm):.2f}s\n")


for track in Track.all_tracks:
    mood = "sad" if track.is_sad() else "not sad"
    print(f"'{track.title}' is {mood} (Key: {track.key_signature})")
