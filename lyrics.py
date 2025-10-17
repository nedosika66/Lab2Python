class Lyrics:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def preview(self, n=10):
        words = self.text.split()
        return " ".join(words[:n]) + ("..." if len(words) > n else "")