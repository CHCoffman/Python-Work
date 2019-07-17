# List of cars, if is an acronym: make uppercase
cars = ['audi', 'bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
# pizza with selected topping. If the topping isn't anchovies, print
# line saying so.	
print("\n")
requested_topping = 'mushrooms'
print("One pizza with " + requested_topping)
if requested_topping != 'anchovies':
	print("Hold the anchovies!")
# Incorrect answer message if not equal to answer.
print("\n")
answer = 17
if answer != 42:
	print("That is not the correct answer, please try again!")
# Checking to see if the user is banned, using if statement
print("\n")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
else:
	print(user.title() + ", you have been banned.")
# Exercises
print("\n")
cat = 'gray'
if cat == 'gray':
	print("Is the cat gray? I think so")
	print(cat == 'gray')
else:
	print("Is the cat black? I don't think so")
	print(cat == 'black')
# 
