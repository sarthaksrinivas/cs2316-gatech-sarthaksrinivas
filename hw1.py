def count_letter(sentence, letter):
	""" Count occurrences of a letter in a sentence, then print out number of occurrences.

	>>> count_letter("so it goes", "s")
	The letter 's' occurs 2 time(s).
	>>> count_letter("Would you kindly", "k")
	The letter 'k' occurs 1 time(s).
	>>> count_letter("CS is sOoOoOo fun!", "o")
	The letter 'o' occurs 6 time(s).
	"""
	sentence = sentence.lower()
	letter = letter.lower()
	counter = 0
	if letter in sentence:
		for character in sentence:
			if letter == character:
				counter += 1
	print("The letter '{}' occurs {} time(s).".format(letter, counter))

def grade_replacement(grade_list):
	""" Return average grade after replacing lowest grade with second lowest grade in a list of grades.

	>>> grade_replacement([100, 90, 80, 70])
	87.5
	>>> grade_replacement([100, 100, 100, 100])
	100.0
	>>> grade_replacement([90, 80, 80, 80, 85])
	85.0
	>>> grade_replacement([30, 80, 44, 80, 85])
	68.6
	"""
	lowest = 100
	for index in range(grade_list):
		if grade_list[index] < lowest:
			lowest = grade
	