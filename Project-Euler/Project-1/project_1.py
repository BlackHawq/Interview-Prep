#Sum of all multiples of 3 and 5 below n

def sum_of_multiples(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:  # Check if the number is a multiple of 3 or 5
            total += i  # Add the multiple to the total
    return total

n = int(input("Enter a number: "))
print(sum_of_multiples(n))
