from functools import total_ordering


@total_ordering
class Day:
    def __init__(self, id):
        self.id = id
        self.signup_library = None
        # Dict[Libray: set[Book]]
        self.scanning_books = {}
    
    def valid(self):
        if self.signup_library:
            if self.signup_library in self.scanning_books:
                print("signing up and scanning the same library")
                return False

        for lib, books in self.scanning_books:
            if len(books) > lib.scans_per_day:
                print("More books than allowed")
                return False
        
        return True

    def __eq__(self, other):
        return self.id == other.id
    def __lt__(self, other):
        return self.id < other.id

class Schedule:
    def __init__(self, total_days):
        self.total_days = total_days
        self.days = [Day(i) for i in range(total_days)]
        self.books_scanned = set()
        self.libraries = []
        self.free_signup_day = self.days[0]

    def score(self):
        return sum(b.score for b in self.books_scanned)
    

    def valid(self):
        if not all(l.valid_signup() for l in self.libraries):
            print("Not all libraries have valid signup periods")
            return False
        if not all(d.valid() for d in self.days):
            print("Not all days are valid")
            return False
        
        return True

    def signup_library(self, lib):
        endday = self.days[self.free_signup_day.id + lib.signup_time]
        assert (endday.id) <= self.total_days
        lib.sigup_assigned = (self.free_signup_day, endday)
        for day in self.days[self.free_signup_day.id:endday.id]:
            day.signup_library = lib
            day.scanning_books = {}
        self.libraries.append(lib)

    def submit_book(self, libray, book, day):
        if libray not in self.libraries:
            raise ValueError("Library not signed up yet")
        day.scanning_books[libray].add(book)

        


