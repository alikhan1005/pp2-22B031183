#      12 * 4 + 23 * 2 = 94
def solve(numheads, numlegs):
    for i in range (numheads):
        if (i * 4) + (numheads-i)*2 == numlegs:
            return i


heads = 35
legs = 94
print(f'count of rabbits {solve(heads, legs)}')
print("count of chikens " + str(35-solve(heads, legs)))