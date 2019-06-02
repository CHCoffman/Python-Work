for value in range(1,5):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

digits = list(range(1,11))
for nums in range(1,11):
	print(min(digits))
	print(max(digits))
	
squares_2 = [value**2 for value in range(1,11)]
print(squares_2)

# Exercises
numbers = list(range(1,21))
print(numbers)

print('\n')

# Print the min, max, and sum of numbers 1-1_000_000
big_numbers = list(range(1,1000001))
for numbers in range(1,2):
	print('min is: ')
	print(min(big_numbers))
	print('\nmax is: ')
	print(max(big_numbers))
	print('\nsum is: ')
	print(sum(big_numbers))
print('\n')

# Find all odd numbers between 1-20
odd_numbers = list(range(1,21,2))
print(odd_numbers)

# Multiples of 3 from 3-30
threes = list(range(3,30,3))
print(threes)

# Cubes from 1-10
cube_numbers = [value**3 for value in range(1,11)]
print(cube_numbers)
