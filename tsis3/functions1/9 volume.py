import math
def volume(r):
    vol = (4/3) * math.pi * (r**3)
    return vol


r = float(input())
print(volume(r))
