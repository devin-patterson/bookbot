from stats import word_counter
from stats import character_counter
from stats import report

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text('./books/frankenstein.txt')
	word_count = word_counter(book_text)
	print(f'Found {word_count} total words')
	character_count = character_counter(book_text)
	print(character_count)
	print(report(character_count))
main()
