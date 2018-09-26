name1 = input("What is your name?").lower().strip()
name2 = input("What the name of the second person?").lower().strip()

if name1 == name2:
	print("You've got the same name")
else: 
	print("You don't have the same name")



if len(name1) == len(name2):
	print(name1 + " contains as much characters as " + name2)
else: 
	print(name1 + " does not contain as much characters as " + name2 )

# Here the difference in characters between the 2 names is calculated
difference = len(name1) - len(name2)


# Because of the difference between the two names can be negative, this new variable makes the negative number positive (deletes the -)
difference_new = abs(difference)

print("Your names have a character difference of " + str(difference_new))

# If the difference in characters is low, the match percentage is higher.
if difference_new < 1:
	print("100% match!")
elif difference_new < 2:
	print("85% match!")
elif difference_new < 3:
	print("75% match!")
elif difference_new < 4:
	print("65% match!")
elif difference_new < 5:
	print("50% match!")
elif difference_new < 6:
	print("40% match!")
elif difference_new < 7:
	print("35% match!")
elif difference_new < 8:
	print("25% match!")
else:
	print("0% match!")
