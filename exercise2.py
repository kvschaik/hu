movies = { 
	"title" : "Interstellar",
	"release" : 2014,
	"duration": 169,
	"director" : "Christopher Nolan"
}

#First part without actors
print("The first part: \n")

for key, value in movies.items():
	print(f'{key.title()}: {value}')


#Second part
print("\n The second part:")

#Add list of actors to movies dictionairy
movies["actors"] = ["Matthew Mcconaughey", "Anne Hathaway", "Jessica Chastain"]

movies["actors"] = ', '.join(movies["actors"])


#Define value so every actor is put in one string so it becomes: actor1, actor2, actor3, etc.
value = ''
for actor in movies["actors"]:
	value = value  + actor + ', '

#Strip the last , from the actors
value = value.strip(", ")



for key, value in movies.items():
	if key == "duration":
		value = f"{value} minutes"
		
	print(f'{key.title()}: {value}')

