def even(n):
    for i in range(0, n):
         if i % 2 == 0:
            yield i


n = int(input())
l = []

for i in even(n):
    l.append(str(i))

print( ", ".join(l) )

