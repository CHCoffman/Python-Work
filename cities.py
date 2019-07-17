# Using flags and breaking loops
prompt = "\nTell me something, and I will repeat it back to you."
prompt += ("\nEnter 'quit' to exit the game")

active = True # as long as active remains true, the loop will continue
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False # active becomes not true, program is inactive
	else:
		print(message)
prompt = "\nEnter the name of a city that you have visited: "
prompt += ("\nEnter 'quit' when you are finished. ")

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I would like to visit " + city.title() + "!")
# Counting
x = 1
while x <=5:
	print(x)
	x += 1
	
o = 25
while o < 30:
	print(o)
	o += 4
