# Summation of primes

def am_i_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    total = 0
    for i in range(2, n):
        if am_i_prime(i):
            total += i
    return total

input_n = int(input("Enter the upper limit for the summation of primes: "))
result = sum_of_primes(input_n)
print(f"The sum of all prime numbers less than {input_n} is: {result}")