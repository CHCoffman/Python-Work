#Methods
# Colten Coffman

# Method that displays a message
def display_message():
	print("I am learning about functions")

display_message()

# Method that displays a method based off of input
def favorite_book(title):
	print("My favorite book is " + title)

favorite_book("The Witcher")

# Method that displays positional arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'lacey')

def make_shirt(shirt_size, shirt_message):
	print("\nYour shirt size will be: " + shirt_size)
	print("Your message will be " + shirt_message)

make_shirt("large", "Hello World")
print("\n")

# Function that accepts a name of a city and its country

def describe_city(city_name, country_name = "Iceland"):
	print(city_name + " is in " + country_name)

describe_city("Reykjavik")
