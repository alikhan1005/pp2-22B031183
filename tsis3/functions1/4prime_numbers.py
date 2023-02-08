def filter_prime(numbers):
    primes = []
    for i in numbers:
        if is_prime(i):
            primes.append(i)

    return primes
      
def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

numbers = []
n = int(input())
while n!=0:
    a = int(input())
    numbers.append(a)
    n -= 1

print(filter_prime(numbers))
