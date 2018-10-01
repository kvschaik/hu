#Creating an empty list
names =[]


#Add names to the list
names.append("Rob")
names.append("David")
names.append("Nick")

#Print the length of the name for every name in the list
for name in names:
    print(len(name))


#Add the lenth and name to a sentence.
for name in names:
    print(name + " bevat " + str(len(name)) + " letters")