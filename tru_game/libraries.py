from dataclasses import dataclass

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
        #tuple of start day and end day inclusive
        self.signup_assigned = tuple()

    def valid_signup(self):
        return (self.signup_assigned[1] - self.signup_assigned[0]) == self.signup_time - 1

    
