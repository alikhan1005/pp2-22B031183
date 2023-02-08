def fahrenheit_to_centigrade(F):
    C = (5/9)*(F - 32)
    return C

f = float(input())
print(f'{f} fahrenheit is {fahrenheit_to_centigrade(f)} celsius')