import sys

infile = open(sys.argv[1], 'r')
oufile = open(sys.argv[2], 'r')

slices, pizza_types = infile.readline().split()
pizza_slices = [int(slices) for slices in infile.readline().split()]
slices = int(slices)
pizza_types = int(pizza_types)

numout = str(oufile.readline())
outvals = [int(slices) for slices in oufile.readline().split()]

outinds = [pizza_slices.index(x) for x in outvals]

# print(outinds)
converted = open('conv' + sys.argv[2], 'w')
converted.write(numout)
converted.write(' '.join(map(str, outinds)))
converted.close()