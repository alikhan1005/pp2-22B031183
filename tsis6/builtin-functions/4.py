import time
import math

def after_milliseconds(n, ms):
    time.sleep(ms/1000)

    sqrt = math.sqrt(n)
    print(f'Square root of {n} after {ms} miliseconds is {sqrt}')


number = int(input())
milliseconds = int(input())
after_milliseconds(number, milliseconds)