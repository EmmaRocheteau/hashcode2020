import sys
from libraries import Book, Library

# parse input into a list of available books and a list of libraries

file = open(sys.argv[1], 'r')

no_books, no_libraries, total_days = [int(x) for x in file.readline().split()]
book_list = [Book(book_id, int(book_score)) for book_id, book_score in enumerate(file.readline().split())]

library_list = []
library_description = True
library_id = 0
for remaining_line in file.readlines():
    if library_description:
        no_books, signup_time, scans_per_day = [int(x) for x in remaining_line.split()]
        library_description = False
    else:
        books_in_lib = [book_list[int(book_id)] for book_id in remaining_line.split()]
        library_list.append(Library(library_id, books_in_lib, signup_time, scans_per_day))
        library_id += 1
        library_description = True

schedule = Schedule(total_days)

#