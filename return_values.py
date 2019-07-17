# Return Values
# Colten Coffman 7/15

# Function takes a first and last name, returns formatted full name

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Using an optional middle name parameter

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + " " + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Return a dictionary

def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)

# Infinite loop~
while True:
	print("\nPlease tell me your name:")
	f_name = input("first_name: ")
	l_name = input("last_name: ")
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
