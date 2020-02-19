import itertools

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def find_max(iterable, target):
    prev_x = 0
    for i, x in enumerate(iterable):
        x += prev_x
        prev_x = x
        # once the limit has been reached with the smallest numbers,
        # we know that anything with more pizzas than i+1 is going to be too big
        if x > target:
            return i + 1

def find_min(iterable, target):
    prev_x = 0
    for i, x in enumerate(reversed(iterable)):
        x += prev_x
        prev_x = x
        # once the solution has been reached with the largest numbers,
        # we know that any solutions with less than i pizzas shouldn't be considered
        # (since i pizzas still doesn't reach the limit - python indexing starts at 0)
        if x > target:
            return i

def smart_powerset(iterable, target):
    s = list(iterable)
    minimum = find_min(iterable, target)
    maximum = find_max(iterable, target)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(minimum, maximum))

def closest(possiblities, target):
    return min((abs(target - total), (o_list, total))
               for o_list, total in possiblities)[1]

def bruteforce(slices, pizza_slices):
    possiblities = []
    for x in smart_powerset(pizza_slices, slices):
        possiblities.append((x, sum(x)))
    pizzas_to_order, score = closest(possiblities, slices)
    no_pizzas = len(pizzas_to_order)
    return (no_pizzas, pizzas_to_order)







