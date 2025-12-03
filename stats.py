def word_counter(text):
        word_list = text.split()
        return len(word_list)

def character_counter(text):
	character_dict = {}
	for word in text:
		for letter in word:
			letter_folded = letter.casefold()
			if letter_folded in character_dict.keys():
                       		character_dict[letter_folded] += 1
			else:
				character_dict[letter_folded] = 1
	return character_dict
		
def report(dict):
	sorted_list = sorted([{"char": char, "num": num} for char, num in dict.items() if char.isalpha()], key=lambda x: x['num'])
        print('============ BOOKBOT ============')
	print(f'Analyzing book found at books/frankenstein')
	print('----------- Word Count ----------')
	return sorted_list				
