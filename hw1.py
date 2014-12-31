def countLetter(sentence, letter):
	""" Count occurrences of a letter in a sentence, then print out number of occurrences.

	>>> countLetter("so it goes", "s")
	The letter 's' occurs 2 time(s).
	>>> countLetter("Would you kindly", "k")
	The letter 'k' occurs 1 time(s).
	>>> countLetter("CS is sOoOoOo fun!", "o")
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

def gradeReplacement(grade_list):
	""" Return average grade after replacing lowest grade with second lowest grade in a list of grades.

	>>> gradeReplacement([100, 90, 80, 70])
	87.5
	>>> gradeReplacement([100, 100, 100, 100])
	100.0
	>>> gradeReplacement([90, 80, 80, 80, 85])
	85.0
	>>> gradeReplacement([30, 80, 44, 80, 85])
	68.6
	"""
	lowest = 100
	for index in range(grade_list):
		if grade_list[index] < lowest:
			lowest = grade