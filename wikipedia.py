import requests
import json

choice = input("What article do you want? ").strip().replace(' ', '_')
language = ["en", "es", "nl"]

#For loop for printing in every language in the variable language
for item in language:
	#{item} places the language to the URL
	#Choice places the user input to the end of the URL
	url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{choice}"
	

	req = requests.get(url)
	data = json.loads(req.text) #loads because of load(string)
	#Print language
	print(f'\n {item}: ')
	#Print title
	print(data["title"])
	#Print extract
	print(data["extract"])
