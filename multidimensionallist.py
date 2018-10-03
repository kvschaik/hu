friends = [
["Nick"],
["Rob"],
["Koen"]
]

#Loop through the friends list
for friend in friends:
	#select the name from the list.
	name = friend[0]
	#Get the length of the name
	length = str(len(name))
	#Add the snack to the multidimensional list
	snack = friend.append(input(name + ", what is your favorite snack? "))
	#Because the variable snack does only append, the snack name is defined by getting the snack from the list friend[1]
	snack_name = friend[1]
	#Print the name, amount of characters and the name of the snack
	print( str(name) + "'s name contains "  + str(length) + " characters and his favorite snack is " + snack_name)




for friend in friends:
	#Get the name from the list
	name = friend[0]
	#Get the snack from the list
	snack = friend[1]
	#Print the sentence containing the name and the snack
	print(name + "'s favorite snack is " + snack)


