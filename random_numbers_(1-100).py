# Generate random number from the range 1-100

# Import random module
import random

# Create the list for the numbers
ran_num = []

# Create the loop for how many number data is needed
for i in range(5):
    # Generate random number from 1-100
    generate_num = random.randint(1,100)
    # To avoid repeating random number
    if generate_num not in ran_num:
        ran_num.append(generate_num)

# Print number
print("Random number in set 1-100:", ran_num)