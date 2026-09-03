#Largest Prime Factor

def am_i_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def what_are_my_Factors(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def largest_prime_factor(n):
    factors = what_are_my_Factors(n)

    for i in range(len(factors)-1, -1, -1):
        if am_i_prime(factors[i]):
            return factors[i]
    return n


n = int(input("Enter a number: "))
print(largest_prime_factor(n))