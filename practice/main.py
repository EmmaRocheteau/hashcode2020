# from brute_force import bruteforce
from example import add
import sys

def subsetsums(slices, pizza_types, pizza_slices):
    for target in range(slices, 0, -1):
        res = add(pizza_slices, pizza_types, target)
        if res:
            return len(res), res
    return 0, []

def blackjack(slices, pizza_types, pizza_slices):
    answer = []
    
    # answer.append(max(pizza_slices))
    sums = 0
    nextval = pizza_slices.pop()
    last_it = False
    while True:
        if not pizza_slices:
            last_it = True
        dif = (slices - (sums + nextval))
        if  dif in pizza_slices:
            answer += [nextval, dif]
            break
        elif dif < 0:
            if pizza_slices:
                nextval = pizza_slices.pop()
            else:
                break
        else:
            answer.append(nextval)
            sums += nextval
        if last_it:
            break
    # while  < slices:
    #     dif = slices - sums
    #     if dif in pizza_slices:
    #         answer.append(dif)
    #         break
    #     else:
    #         newval = pizza_slices.pop()
    #         sums += newval
    #         slices -= newval
    #         answer.append(newval)
    return len(answer), answer
 
# parent_dir = '/Users/emmarocheteau/PycharmProjects/hashcode2020/practice/'
# a_example = open('{}a_example.in'.format(parent_dir))
# b_small = open('{}b_small.in'.format(parent_dir))
# c_medium = open('{}c_medium.in'.format(parent_dir))
# d_quite_big = open('{}d_quite_big.in'.format(parent_dir))
# e_also_big = open('{}e_also_big.in'.format(parent_dir))


input = open(sys.argv[1], 'r')

slices, pizza_types = input.readline().split()
pizza_slices = [int(slices) for slices in input.readline().split()]

slices = int(slices)
pizza_types = int(pizza_types)

no_pizzas = 0
pizzas_to_order = []

# all functions should have the form:
# def solution(slices, pizza_types, pizza_slices):
#     return no_pizzas, pizzas_to_order

# no_pizzas, pizzas_to_order = bruteforce(slices, pizza_slices)
no_pizzas, pizzas_to_order = blackjack(slices, pizza_types, pizza_slices)
print(sum(pizzas_to_order), slices)
output = open('black_{}.out'.format(input.name[:-3]), 'w')
output.write(str(no_pizzas) + '\n')
output.write(' '.join(map(str, pizzas_to_order)))
output.close()