

class Day:
    def __init__(self, id):
        self.id = id
        self.signup_library = None
        # Dict[Libray: set[Book]]
        self.scanning_books = {}
    
    def valid(self):
        if self.signup_library:
            if self.scanning_books:
                print("signing up and scanning")
                return False

        for lib, books in self.scanning_books:
            if len(books) > lib.scans_per_day:
                print("More books than allowed")
                return False
        
        return True


class Schedule:
    def __init__(self, total_days):

        self.daya = [Day(i) for i in range(total_days)]
        self.books_scanned = set()
    
    def score(self):
        return sum(b.score for b in self.books_scanned)

