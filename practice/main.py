a_example = open('a_example.in')
b_small = open('b_small.in')
c_medium = open('c_medium.in')
d_quite_big = open('d_quite_big.in')
e_also_big = open('e_also_big.in')

input = a_example

slices, pizza_types = input.readline().split()
pizza_slices = [int(slices) for slices in input.readline().split()]

no_pizzas = 0
pizzas_to_order = []

# solution here

output = open('{}.out'.format(input.name[:-3]), 'w')
output.write(str(no_pizzas) + '\n')
output.write(' '.join(map(str, pizzas_to_order)))
output.close()