from functools import total_ordering


def score(books):
    return sum(b.score for b in books)

@total_ordering
class Day:
    def __init__(self, id):
        self.id = id
        self.signup_library = None
        # Dict[Library: set[Book]]
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
    def __init__(self, total_days, unused_libraries):
        self.total_days = total_days
        self.days = [Day(i) for i in range(total_days)]
        self.books_scanned = set()
        self.signed_libraries = []
        self.unused_libraries = unused_libraries
        self.free_signup_day = self.days[0]

    def score(self):
        return score(self.books_scanned)
    

    def valid(self):
        if not all(l.valid_signup() for l in self.signed_libraries):
            print("Not all signed_libraries have valid signup periods")
            return False
        if not all(d.valid() for d in self.days):
            print("Not all days are valid")
            return False
        
        return True

    def signup_library(self, lib):
        endday = self.days[self.free_signup_day.id + lib.signup_time]
        assert (endday.id) <= self.total_days
        lib.signup_assigned = (self.free_signup_day, endday)
        for day in self.days[self.free_signup_day.id:endday.id]:
            day.signup_library = lib
            day.scanning_books = {}
        self.signed_libraries.append(lib)
        self.free_signup_day = endday

    def submit_book(self, library, book, day):
        library.books.remove(book)
        if library not in self.signed_libraries:
            raise ValueError("Library not signed up yet")
        day.scanning_books[library].add(book)
        for lib in self.unused_libraries:
            if book in lib.books:
                lib.books.remove(book)
    
    def library_summaries(self):
        sumas = {lib: [] for lib in self.signed_libraries}
        for day in self.days:
            for lib, books in day.scanning_books.items():
                sumas[lib] += list(books)
        
        return sumas




