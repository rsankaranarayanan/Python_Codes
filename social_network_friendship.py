# Write a social network with two methods:

# 1. add friend - takes two strings name1 and name2 as input and makes them friends, returns void.
# 2. AretheyInSamecircle - takes two strings name1 and name2 as input and returns true if they are directly or indirectly friends return true.
# returns false if they have no one in common.

# eg: If A is friends with B, B is friends with C, C is friends with D. X is friends with Y.
# AretheyInSamecircleA,B ->true
# AretheyInSamecircleA,D -> true
# AretheyInSamecircle A,X -> false

# Friendships are bidirectional

# a is friends iwth B implies B is friends with A

# you can assume all people are unique.
# friends_array = [['a', 'b'], ['c', 'd'],  ['b','c'], ['d', 'e'], ['x', 'y']]
import argparse
import sys

def collect_friendship(number_of_friends_group):
	friends_list = list()
	count = 1
	while 0 < number_of_friends_group:
		temp_list = list()
		print("Enter the Friend Name 1 for {0} group.".format(count))
		fri1 = input()
		print("Enter the Friend Name 2 for {0} group.".format(count))
		fri2 = input()
		if fri1 == fri2:
			sys.exit("{0} and {1} are same value in {3} group. Re-execute this script and Enter the different values".format(fri1,fri2,count))
		temp_list.append(fri1)
		temp_list.append(fri2)
		friends_list.append(temp_list)
		number_of_friends_group -=1
		count += 1
	return friends_list


def check_friendship_link(number_of_list, friend1, friend2):
	friends_array = collect_friendship(number_of_list)
	if friend1 == friend2:
		print("The {0} friend1 and {1} friend2 are same value.".format(friend1, friend2))
		sys.exit(1)
	temp_dict = dict()
	for fr in friends_array:
		for i in fr:
			temp_dict[i] = list()

	for fr1 in friends_array:
		for ii in fr1:
			for k in temp_dict.keys():
				if str(ii) in str(k):
					temp_dict[k].append(fr1[0])
					temp_dict[k].append(fr1[1])
					temp_dict[k] = list(set(temp_dict[k]))
					
	for r in range(0,len(friends_array)):
		for fr1 in friends_array:
			for ii in fr1:
				for k in temp_dict.keys():
					if str(ii) in str(temp_dict[k]):
						temp_dict[k].append(fr1[0])
						temp_dict[k].append(fr1[1])
						temp_dict[k] = list(set(temp_dict[k]))
	print(temp_dict)
	if friend1 in temp_dict.keys():
		print(temp_dict[friend1])
		if friend2 in str(temp_dict[friend1]):
			print("{0} and {1} are friends.".format(friend1, friend2))
		else:
			print("{0} and {1} are not friends.".format(friend1, friend2))
	else:
			print("{0} and {1} are not friends.".format(friend1, friend2))

def main():
	parser = argparse.ArgumentParser(description='Friends List Creation and Find Firends Map')
	parser.add_argument('--nogroup', dest='nogroup', type=int, help='Name of the group', required=True)
	parser.add_argument('--fri1', dest='fri1', help='Enter the First Friend Name', required=True)
	parser.add_argument('--fri2', dest='fri2', help='Enter the Second Friend Name', required=True)

	args = parser.parse_args()
	check_friendship_link(args.nogroup, args.fri1, args.fri2)
	


if __name__ == main():
	main()


