#Largest Palindrome

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n):
    largest = 0
    track = 0
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
            elif is_palindrome(product) and product <= largest:
                track += 1
                if track == 25:
                    return largest
    return largest

input_number = int(input("Enter a number: "))
result = largest_palindrome_product(input_number)
print(f"The largest palindrome product of two {input_number}-digit numbers is: {result}")