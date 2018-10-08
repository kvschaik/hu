import json

with open("movies.json") as f:
	movies = json.load(f)

user_year = int(input("From what year do you want to display?"))

for movie in movies:
	year = movie["year"]
	title = movie["title"]
	if year == user_year:
		print(f'The movie {title} is from the year {year}')
        
        
        
for movie in movies:
    director = movie["director"]
    actor = movie["actors"]
    if movie["director"] in actor:
        print(f'In the movie {movie["title"]}, the director {director} is also an actor')
        
        
director = input("From which director do you want to know his/her movies? ")

for movie in movies:
    if director.lower() == movie["director"].lower():
        print(f'Director {movie["director"]} made the movie:  {movie["title"]}')


