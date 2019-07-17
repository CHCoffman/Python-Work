# Python dictionaries, examples and exercises

alien_0 = {'color':'green', 'points': 5} # 'color' and 'points' are keys, green and 5 values
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " +str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
# modifying values in an entry
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'blue'
print("The alien is now " + alien_0['color'] + ".")

# tracking the position of alien at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3

# The new alien position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removing key value pairs
del alien_1['points']
print(alien_1)
print("\n")

# Favorite language poll
favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("sarah's favorite language is " + favorite_language['sarah'].title() +
".")

#for name in favorite_language:
	#print(name.title())
friends = ['phil', 'sarah']
for name in favorite_language.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_language[name].title() + "!")
	else:
		print(name.title() + " please take our poll!")
print("the following languages have been mentioned:")
for language in set(favorite_language.values()):
	print(language.title())
	
print("\n")
# Exercises
natalie_coffman = {
	'first_name': 'natalie', 'last_name': 'coffman',
	'age': 23, 'city': 'austin'}
print(natalie_coffman)
favorite_numbers = {
	'natalie': 3,
	'brycen': 55,
	'colten': 12,
	'angi': 23,
	}

print("People and their fav numbers: " + str(favorite_numbers))
glossary = { 
	'key': ': data point which the value will be linked to.',
	'value': ': the value of the key in a dictionary.',
	'dictionary': ': holds data that is defined.',
	}
print("\n")
print("Key" + glossary['key'])
print("Value" + glossary['value'])
print("Dictionary" + glossary['dictionary'])
print("\n")
# Looping through a dictionary
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for k, v in user_0.items():
	print("\nKey: " + k)
	print("Value: " + v)
