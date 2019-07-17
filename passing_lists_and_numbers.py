# Colten Coffman 7/17/19
# Passing lists and numbers to methods
def greet_users(names):
	"""Print a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Simulate creating a 3D print from the design.
	print("Printing model: " + current_design)
	completed_models.append(current_design)
	
# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

# Exercise: make magicians, pass to list and display with a function
print()
magicians = ['Houdini', 'blane', 'copperfield']
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
def make_great(magicians):
	for magician in magicians:
		print(magician.title() + " The Great")

show_magicians(magicians)
print()
make_great(magicians)

# Passing arbitrary numbers of arguments

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
