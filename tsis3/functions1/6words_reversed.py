def reversed(senten):
    words = senten.split()
    n = len(words)
    rever = []
    while (n>0):
        n -=1
        rever.append(words[n])

    
    return rever


s = input()
print (' '.join(reversed(s)))