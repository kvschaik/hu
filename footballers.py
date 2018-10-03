f = open("footballers.csv")
fn = open("footballersnew.csv", "w")

for line in f:
	row = line.split(",")
	player = row[0]
	club = row[1]
	sold = row[2]
	print(player + " has been sold for the insane amount of " + sold + " million to " + club)
	sold_new = int(sold) * 1000000
	row_new = player + "," + club + "," + str(sold_new) + "\n"
	fn.write(row_new)

player = input("What is the name of the player? ")
club = input("What is the name of the club? ")
sold = int(input("For how much dollar is he sold? (In millions) ")) 
sold_new = str(sold * 1000000)


row_new = player + "," + club + "," + sold_new + "\n"
fn.write(row_new)




fn.close()

f.close()
