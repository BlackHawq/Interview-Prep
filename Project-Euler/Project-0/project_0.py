#Calculate the Sum of odd squares up to n

def sum_of_odd_squares(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            total += i ** 2  # Add the square of the odd number to the total
    return total

n = int(input("Enter a number: "))

print(sum_of_odd_squares(n))
input("Press Enter to exit...")
