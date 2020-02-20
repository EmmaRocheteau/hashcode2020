import itertools

def brute(schedule):
    def total_lenghth_filt(liblist):
        return sum(l.signup_time for l in liblist) <= schedule.total_days
    
    alllibs = schedule.unused_libraries

    all_lib_perms = itertools.permutations(alllibs)

    all_lib_perms = filter(total_lenghth_filt, all_lib_perms)

    