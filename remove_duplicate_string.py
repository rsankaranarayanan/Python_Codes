firststring = "aaabbcdefghijjkkllma"
splitstring = []
for i in firststring:
	splitstring.append(i)


slength = len(splitstring)
for i in range(0, slength):
	for j in range(0, slength):
		if splitstring[i] < splitstring[j]:
			tempvar = splitstring[j]
			splitstring[j] = splitstring[i]
			splitstring[i] = tempvar


uniquestring = ""
for i in range(len(splitstring)):
	if splitstring[i] in splitstring[i+1:]:
		pass
	else:
		uniquestring += splitstring[i]


print(uniquestring)