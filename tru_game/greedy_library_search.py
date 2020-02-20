def main(schedule):
    for l in schedule.unused_libraries:
        l.sort_books()
    greedy_library_search(schedule)
    return schedule


def greedy_library_search(schedule):
    # function has to choose library from the list of non used libraries, and then calculate the updated schedule
    prev_pot_score = 0
    for l in schedule.unused_libraries:
        remaining_time = schedule.free_signup_day - l.signup_time
        max_books_scanned = min(remaining_time * l.scans_per_day)
        pot_score = l.score(max_books_scanned)
        if pot_score > prev_pot_score:
            chosen_library = l


    if schedule.free_signup_day.id - schedule.total_days > 0:
        greedy_library_search(schedule)