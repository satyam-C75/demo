#Satyam
def printa(a):
    for i in 10:
        print(a[i])

#Peeyush 
#adding 10 numbers
def add_numbers(start, end):
  total = 0
  for num in range(start, end + 1):
    total += num
  return total

sum_of_numbers = add_numbers(1, 10)
print("Sum of numbers from 1 to 10:", sum_of_numbers)
#rishabh
import random

# Generate 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the average
average = sum(random_numbers) / len(random_numbers)

# Print the results
print("Random Numbers:", random_numbers)
print("Average:", average)

