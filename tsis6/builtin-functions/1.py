# import numpy
# result1 = numpy.prod(list1)
# 2. result1 = math.prod(list1)
# 3. m = mul(i, m)
# 4. result1 = reduce((lambda x, y: x * y), list1)

# import math
# import numpy

def product(l):
    prd = 1
    for i in l:
        prd *= i
    return prd

l = []
n = int(input())
while n > 0:
    a = int(input())
    l.append(a)
    n-=1
print(product(l))