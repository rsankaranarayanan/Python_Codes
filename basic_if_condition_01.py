# 1. We are having 3 list like this

# Colors = [“Yellow”,”Green”,”White”,”Black”]

# Fruits=[“Apple”,”Papaya”,”Mango”,”Orange”]

# Animals=[“Tiger”,”Lion”,”Deer”,”Zebra”]

#   i. Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , like its is a fruit or color or Animal

#  ii. Write a program that asks user to enter two items and it tells you if they both are in same category or not. For example if I enter yellow and Black, it will print "Both are colors" but if I enter yellow and Tiger it should print "They don't belong to same category"


Colors = ["Yellow","Green","White","Black"]

Fruits=["Apple","Papaya","Mango","Orange"]

Animals=["Tiger","Lion","Deer","Zebra"]

userinput = input()

if userinput.lower() in str(Colors).lower():
	print("{0} belongs to {1} category.".format(userinput, "Colors"))
elif userinput.lower() in str(Fruits).lower():
	print("{0} belongs to {1} category.".format(userinput, "Fruits"))
elif userinput.lower() in str(Animals).lower():
	print("{0} belongs to {1} category.".format(userinput, "Animals"))
else:
	print("{0} is not belong to Colors, Fruits and Animals category.".format(userinput))

print("Enter the Item01")
uinput01 = input()
print("Enter the Item02")
uinput02 = input()

def categroy_belongs(s):
	if s.lower() in str(Colors).lower():
		return "Colors"
	elif s.lower() in str(Fruits).lower():
		return "Fruits"
	elif s.lower() in str(Animals).lower():
		return "Animals"
	else:
		return "NoCategroy"

u01_categroy = categroy_belongs(uinput01)
u02_categroy = categroy_belongs(uinput02)


if u01_categroy != "NoCategroy" and u02_categroy != "NoCategroy":
	if u01_categroy == u02_categroy:
		print("{0} and {1} are same categroy.".format(uinput01, uinput02))
	else:
		print("{0} and {1} are not same categroy.".format(uinput01, uinput02))
else:
	print("{0} and {1} are not same categroy.".format(uinput01, uinput02))