import math
sides = int(input())
length = int(input())

area = (sides/4) * length**2 / math.tan(math.pi/sides)
print(round(area))