#create a list without any names.
names = []

#add names to list
names.append("Rob")
names.append("David")
names.append("Nick")

#ask the user for their name and add it to the list. .title() makes the first character an uppercase
names.append(input("What's your name? ").title())


#create a list without any snacks.
snacks = []


#Add some snacks to the list
snacks.append("Snickers")
snacks.append("Oreo")
snacks.append("Twix")


#ask the user for their favorite snack .title() makes the first character an uppercase
snacks.append(input("What's your favorite snack? ").title())

#Index will be the number for the snacks list. snacks[index] = snacks[0]. Then 1 is added to [index] so snacks[index] becomes snacks[1] and so on.
index = 0
for name in names:
	print(name + "'s favorite snack is a " + snacks[index])
	index = index +1


