# Trying out the Sieve of Eratosthenes

def nth_prime(n):
    if n < 1:
        raise ValueError("n must be at least 1")

    # Rough upper bound for the nth prime
    if n < 6:
        limit = 15
    else:
        import math
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            # p*p and everything after it that is a multiple of p
            sieve[p * p : limit + 1 : p] = [False] * (
                ((limit - p * p) // p) + 1
            )

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    return primes[n - 1]

num = int(input("Enter the position of the prime number you want: "))
print(f"The {num}th prime number is: {nth_prime(num)}")