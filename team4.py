#Satyam
def printa(a):
    for i in 10:
        print(a[i])

#rishabh
import random

# Generate 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the average
average = sum(random_numbers) / len(random_numbers)

# Print the results
print("Random Numbers:", random_numbers)
print("Average:", average)