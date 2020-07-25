class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.post = []

    def __repr__(self):
        return f"{self.title} by {self.author} ({len(self.post)} post{'s' if len(self.post) > 1 else ''})"
