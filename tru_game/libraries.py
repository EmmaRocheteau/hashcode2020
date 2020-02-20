from dataclasses import dataclass

@dataclass
class Book:
    id: int
    score: int

@dataclass
class Library:
    id: int
    books: set
    signup_time: int
    scans_per_day: int


