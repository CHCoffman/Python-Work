# List and list methods examples
# Colten Coffman

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
message = "My first bicycle was a " + bicycles[0].title()
print(message)

names = ['Brycen', 'Natalie', 'Cade', 'Rylee']
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])

ry_message = names[-1] +' is my little sister'
print(ry_message)

nat_message = 'My fiance is named ' + names[1]
print(nat_message)

names[-1] = names[0]
print(names)

names.append('Angi')
print(names)

cars = []
print(cars)

cars.append('Mazerati')
cars.append('Honda')
cars.append('Ford')
print(cars)
cars.insert(0, 'Toyota')
print(cars)

del cars[2]
print(cars)

popped_car = cars.pop()

print(cars)
print(popped_car)

too_expensive = 'Mazerati'
cars.remove(too_expensive)
print(cars)
print("A " + too_expensive.title() + " is too expensive for me")


# Exercises 3-4-3-7
dinner_guests = ['Abraham Lincoln', 'RDJ', 'Arnold Schwarzeneggar']
print(dinner_guests)
print(dinner_guests[0] + " Freed the slaves!")
print(dinner_guests[1] + " is Iron man")
print(dinner_guests[2] + " is my personal hero!")
print(dinner_guests[0] + " can't make it, due to the fact that he is dead")
dinner_guests.remove('Abraham Lincoln')
dinner_guests.insert(0, 'Gary Coffman')
print(dinner_guests)

print(dinner_guests[0] + " is my dad!")
print(dinner_guests[1] + " is Iron Man!")
print(dinner_guests[2] + " is my personal hero!")
dinner_guests.insert(0, 'Spider-Man')
dinner_guests.insert(2, 'Thor')
dinner_guests.append('The Hulk')
print(dinner_guests)

print('We can only invite three people!')
popped_guest = dinner_guests.pop(0)
print('Sorry, ' + popped_guest + ' I have to uninvite you')
popped_guest_1 = dinner_guests.pop(1)
print('Sorry, ' + popped_guest_1 + ' I have to uninvite you')
popped_guest_2 = dinner_guests.pop(2)
print('Sorry, ' + popped_guest_2 + ' I have to uninvite you')
print(dinner_guests)

del dinner_guests[0]
del dinner_guests[1]
dinner_guests.remove('RDJ')
print(dinner_guests)

# Sorting exercises and examples
new_cars = ['bmw', 'audi', 'toyota', 'subaru']
#new_cars.sort()
#print(new_cars)
#new_cars.sort(reverse=True)
#print(new_cars)

print("Here is the original list: ")
print(new_cars)
print("\nHere is the sorted list: ")
print(sorted(new_cars))
print("\nHere is the original list again: ")
print(new_cars)

new_cars.reverse()
print(new_cars)
print(len(new_cars))

