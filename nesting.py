# Creating dictionary entries for aliens and making them into a list
# Colten Coffman 6/11/2019
#alien_0 = {'color': 'green', 'points':5}
#alien_1 = {'color': 'yellow', 'points':10}
#alien_2 = {'color': 'red', 'points':15}

#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#	print(alien)

# Making an empty list for storing aliens
aliens = []

# Make 30 aliens
for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Shows the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# A list in a dictionary
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)
	
favorite_language = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_language.items():
	print("\n" + name.title() +"'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

