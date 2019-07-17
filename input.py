message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Printing a user's inputted name
name = input("What is your name? ")
print("Hello " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print("\nHello, " + name + "!")

# Rollercoaster height
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride the ride!")
else:
	print("You aren't tall enough to ride the ride.")

# Determining whether or not a number is even
number = input("Enter a number, and I'll tell you if it's even  or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

# Exercises
# Rental car
car_type = input("What kind of car would you like? ")
print("Ok, let's see if we can find you a " + car_type)

# Restaurant seating
dinner_group = input("How many in your party? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
	print("\nThere will be a small wait.")
else:
	print("\nRight this way!")
