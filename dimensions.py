dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#exercises
print("\n")
foods = ('big mac', 'royale w cheese', 'fries', 'apple pie', 'nuggs')
print(foods)

name = 'jamie'
if name == 'john':
	print('hello john')
elif name == 'brian':
	print('hello brian')
else:
	print('unknown')
# Testing multiple conditions
print('\n')
requested_toppings = ['extra cheese', 'mushrooms']
if 'mushrooms' in requested_toppings:
	print('adding mushrooms')
if 'pepperoni' in requested_toppings:
	print('adding pepperoni')
if 'extra cheese' in requested_toppings:
	print('adding extra cheese')
print("\nFinished making your pizza!")
# Alien Game Exercise
alien_color = 'yellow'
if alien_color == 'green':
	print("+5 points for shooting down the alien!")
elif alien_color == 'red':
	print("+10 points for destroying the craft!")
else:
	print("Alien survived!")
#if-else statements with requested toppings
requested_toppings = ['mushrooms', 'green_peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green_peppers':
		print("I'm sorry, we are all out of green peppers right now!")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# Availability and requested toppings
print('\n')
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we do not have " + requested_topping + ".")
print("\nFinished making your pizza!")
