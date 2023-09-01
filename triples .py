lines = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
triples = []
for line in lines:
	for i in range(len(line)-2):
		triples.append(line[i:i+3])

print(triples)
