def greedy(schedule):
    for l in schedule.unused_libraries:
        l.sort_books()
    greedy_library_search(schedule)
    return schedule


def greedy_library_search(schedule):
    # function has to choose library from the list of non used libraries, and then calculate the updated schedule
    prev_pot_score = 0
    for l in schedule.unused_libraries:
        remaining_time = schedule.free_signup_day.id - l.signup_time
        if remaining_time < 0:
            continue
        max_books_scanned = min(remaining_time * l.scans_per_day, len(l.books))
        pot_score = l.score(max_books_scanned)
        if pot_score > prev_pot_score:
            chosen_library = l
            books_for_scan = l.books[:max_books_scanned]
            prev_pot_score = pot_score
    if prev_pot_score > 0:
        schedule.signup_library(chosen_library)
        day = chosen_library.signup_assigned[1]
        day_tracker = day.id
        for i, book in enumerate(books_for_scan):
            schedule.submit_book(chosen_library, book, day)
            if i % chosen_library.scans_per_day == 0:
                day_tracker += 1
                day = schedule.days[day_tracker]

    if schedule.free_signup_day.id - schedule.total_days > 0:
        greedy_library_search(schedule)