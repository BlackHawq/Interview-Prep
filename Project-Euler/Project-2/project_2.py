#Sum of even Fib below n

def even_fib_sum(n):
    a, b = 0, 1
    out = 0
    while b <= n:
        if b % 2 == 0:
            out += b
        a, b = b, a + b
    return out

n = int(input("Enter a number: "))
print(even_fib_sum(n))