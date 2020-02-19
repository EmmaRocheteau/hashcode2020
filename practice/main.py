from brute_force import bruteforce

parent_dir = '/Users/emmarocheteau/PycharmProjects/hashcode2020/practice/'
a_example = open('{}a_example.in'.format(parent_dir))
b_small = open('{}b_small.in'.format(parent_dir))
c_medium = open('{}c_medium.in'.format(parent_dir))
d_quite_big = open('{}d_quite_big.in'.format(parent_dir))
e_also_big = open('{}e_also_big.in'.format(parent_dir))

input = c_medium

slices, pizza_types = input.readline().split()
pizza_slices = [int(slices) for slices in input.readline().split()]

slices = int(slices)
pizza_types = int(pizza_types)

no_pizzas = 0
pizzas_to_order = []

# all functions should have the form:
# def solution(slices, pizza_types, pizza_slices):
#     return no_pizzas, pizzas_to_order

no_pizzas, pizzas_to_order = bruteforce(slices, pizza_slices)

output = open('{}.out'.format(input.name[:-3]), 'w')
output.write(str(no_pizzas) + '\n')
output.write(' '.join(map(str, pizzas_to_order)))
output.close()