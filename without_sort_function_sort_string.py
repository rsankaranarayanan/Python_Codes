firststring = "bacadg"
splitstring = []
slength = len(firststring)
for i in firststring:
	splitstring.append(i)


for i in range(0, slength):
	for j in range(0, slength):
		if splitstring[i] < splitstring[j]:
			tempvar = splitstring[j]
			splitstring[j] = splitstring[i]
			splitstring[i] = tempvar


print("".join(splitstring))