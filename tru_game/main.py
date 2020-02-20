import sys
from libraries import Book, Library

file = open(sys.argv[1], 'r')

no_books, no_libraries, no_days = file.readline().split()
book_list = [Book(book_id, int(book_score)) for book_id, book_score in enumerate(file.readline().split())]

library_list = []
library_desc = True
for remaining_line in file.readlines():
    if library_desc:
        books, signup_process, days = remaining_line
        library_desc = False
    else: 