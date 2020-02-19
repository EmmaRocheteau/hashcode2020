import itertools

def powerset(iterable):
    '''powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'''
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def closest(possiblities, target):
    return min((abs(target - total), (o_list, total))
               for o_list, total in possiblities)[1]

def bruteforce(slices, pizza_slices):
    possiblities = []
    for x in powerset(pizza_slices):
        possiblities.append((x, sum(x)))
    pizzas_to_order, score = closest(possiblities, slices)
    no_pizzas = len(pizzas_to_order)
    return (no_pizzas, pizzas_to_order)







