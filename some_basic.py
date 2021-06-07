#1. Return the sequre of odd number between 10 and 20

for i in range(12,21,2):
	print((i-1) * (i-1))

#2. Return every 2nd element in a list between 2 indices

given_list = [1,2,3,4,5,6,7,8,9,10]

given_list[3:6:2]

#3. How to find the largest and lowest value in the list?

lst = [1,2,3,4,5]

print(min(lst))

print(max(lst))

#Write a Python Program to sort (ascending and descending) a dictionary by value.

x = {'A':5,'B':4,'C':2,'D':6,'E':3}
asc = sorted(x.items(), key=operator.itemgetter(1))
print('Ascending Order Is : ',asc)

desc = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print('Descending Order Is : ',desc)

