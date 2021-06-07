# Write Square shape.
print("Enter the number")
uinput = int(input())

inner_space = (uinput - 2)*2
print("* " * uinput)
for i in range(1,uinput-1):
	print("* " + " " * inner_space + "*")
print("* " * uinput)

