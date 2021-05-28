def find_pair(target, listvalue):
	temp_list = list()
	for i in listvalue:
		temp_sum = target - i
		if temp_sum in listvalue:
			t_list = [i, temp_sum]
			temp_list.append(t_list)

	if temp_list:
		print(temp_list)
	else:
		print("No Pair found")

listvalue =  [2,3,15,14,10,11]
find_pair(1, listvalue)