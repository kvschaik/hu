movies = { 
	"title" : "Interstellar",
	"release" : 2014,
	"duration": 169,
	"director" : "Christopher Nolan"
}

'''
for movie, value in movies.items():
	print(movie, value)

'''
for movie,value in movies.items():
	print(f'{movie}: {value}')

