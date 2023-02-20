def divisible(n):
    for i in range(n):
         if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
l = []

for i in divisible(n):
    l.append(str(i))

print( ", ".join(l) )