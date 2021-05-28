sortlist = [3,10,4,6,8,9,9]
slength = len(sortlist)


for i in range(slength):
	for j in range(slength):
		if sortlist[i] < sortlist[j]:
			tempvar = sortlist[j]
			sortlist[j] = sortlist[i]
			sortlist[i] = tempvar


print(sortlist)