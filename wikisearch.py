import wikipedia

while True:
	query=input("search: ")

	print(wikipedia.summary(query))	