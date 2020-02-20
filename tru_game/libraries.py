class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Library:
    def __init__(self, id, books, signup_time, scans_per_day):
        self.id = id
        self.books = books
        self.signup_time = signup_time
        self.scans_per_day = scans_per_day



