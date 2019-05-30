#Python tells the comp to take each element in the list and store it 
# in the variable magician. It then loops through doing the same with all.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print('Thank you, everyone! That was a great show!')
