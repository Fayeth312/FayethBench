import random
with open("sowpods.txt", "r") as f: 
	allText = f.read() 
	words = list(map(str, allText.split())) 
	print(random.choice(words))