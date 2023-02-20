def generator(N):
    for i in range(1, N+1):
        yield i*i

for i in generator(8):
    print(i)