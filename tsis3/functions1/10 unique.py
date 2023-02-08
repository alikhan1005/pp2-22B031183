def unique(l):
    unique_el = []
    for i in l:
        if i not in unique_el:
            unique_el.append(i)
    return unique_el





n = int(input())
l = []
while n>0:
    a = int(input())
    l.append(a)
    n-=1

print(unique(l))
