# Write the Reverse order in the give sentenance 

# Input String = "This is my sample code"
# Output String = "code sample my is This"


istring = input()

ostring = istring.split()[::-1]

output_string = str()
for os in ostring:
	output_string += os + " "

print(output_string)