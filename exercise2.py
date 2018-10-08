movies = { 
	"title" : "Interstellar",
	"release" : 2014,
	"duration": 169,
	"director" : "Christopher Nolan"
}

#First part without actors
print("The first part: \n")

print(f'The title is {movies["title"]}')
print(f'The release year is {movies["release"]}')
print(f'The duration is {movies["duration"] + 117} minutes')
print(f'The director is {movies["director"]}')


#Second part
print("\n The second part:")

#Add list of actors to movies dictionairy
movies["actors"] = ["Matthew Mcconaughey", "Anne Hathaway", "Jessica Chastain"]

#Define value so every actor is put in one string so it becomes: actor1, actor2, actor3, etc.
value = ''
for actor in movies["actors"]:
	value = value  + actor + ', '

#Strip the last , from the actors
value = value.strip(", ")


print(f'The title is {movies["title"]}')
print(f'The release year is {movies["release"]}')
print(f'The duration is {movies["duration"] + 117} minutes')
print(f'The director is {movies["director"]}')
print("Actors: " + value)
