firststring = ["b","a","c", "a","d", "g"]
slength = len(firststring)
for i in range(0, slength):
	for j in range(0, slength-1):
		if firststring[i] < firststring[j]:
			tempvar = firststring[j]
			firststring[j] = firststring[i]
			firststring[i] = tempvar


print(firststring)