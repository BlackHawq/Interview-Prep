#smallest number that is evenly divisible by all of the numberrs up to n

def smallest_divisible(n):
    result = 1
    guess = 1
    while result == 1:
        guess += 1
        for i in range(1,n+1):
            if guess % i != 0:
                break
            if i == n:
                result = guess
    return result

on = int(input("Enter a number: "))
print(smallest_divisible(on))