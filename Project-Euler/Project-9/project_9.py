# Pythagorean Triplet

def find_pythagorean_triplet(sum_value):
    for i in range(1,sum_value):
        for j in range(i+1, sum_value):
            k = sum_value - i - j
            if i**2 + j**2 == k**2:
                print(i*j*k)
                return (i, j, k)
    return None
input_sum = int(input("Enter the sum of the Pythagorean triplet: "))
triplet = find_pythagorean_triplet(input_sum)
print(f"The Pythagorean triplet for the sum {input_sum} is: {triplet}")