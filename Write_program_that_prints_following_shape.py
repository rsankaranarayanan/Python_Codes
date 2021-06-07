# Write a program that prints following shape

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# *


print("Enter the number to draw shape")
uinput = int(input())

for i in range(int(uinput) + 1):
	print("* " * i)
for i in range(int(uinput) - 1,-0,-1):
	print("* " * i)
