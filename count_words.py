#Count the word in the given lines:

#Input String: "Apple APPLE Apple Hello beginner."
#Output String:
# Apple 2
# APPLE 1
# Hello 1
# beginner. 1

def count_words(s):
	remove_duplicate_word = set(s.split())
	for rpd in remove_duplicate_word:
		globals()[rpd] = 0

	for word in s.split():
		for rpd in remove_duplicate_word:
			if str(word) == str(rpd):
				globals()[rpd] += 1

	for rp in remove_duplicate_word:
		print(rp, globals()[rp])

count_words("Apple APPLE Apple Hello beginner.")
