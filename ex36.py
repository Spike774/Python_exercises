# Huanging man
# 2015-01-19 released by Noir Wu
# noir.wu@foxmail.com
import random
lives_remain = 14
words = ['cat', 'dog', 'cheeze', 'hello', 'naive', 'giraff']
guessed_letters = ' '

def play():
	word = get_word()
	while True:
		guess = get_guess(word)
		if process_guess(guess, word):
			print "You win, good job!"
			break
		if lives_remain == 0:
			print "You are hung, good job!"
			print "The word is: " + word
			break
			
def get_word():
	#flag = raw_input('Please set a word or use the default word lab...')
	#if flag != None:
	#	word = flag
	#else:
	word = words[random.randint(0,len(words) - 1)]
	return word
	
def get_guess(word):
	print_word_with_blanks(word)
	print 'lives remain: %d' % lives_remain
	guess = raw_input(' Guess a letter or whole word:')
	return guess
	
def print_word_with_blanks(word):
	display_word = ' '
	for letter in word:
		if (guessed_letters.lower()).find(letter.lower()) > -1:
			display_word = display_word + letter
		else:
			display_word = display_word + '-'
	print display_word
	
def process_guess(guess, word):
	if len(guess) > 1:
		return whole_word_guess(guess, word)
	else:
		return single_word_guess(guess, word)

def whole_word_guess(guess, word):
	global lives_remain
	if guess.lower() == word.lower():
		return True
	else:
		lives_remain -= 1
		return False
	
def single_word_guess(guess, word):
	global lives_remain
	global guessed_letters
	if (word.lower()).find(guess.lower()) == -1:
		lives_remain -= 1 
	guessed_letters += guess
	if all_letter_guessed(word):
		return True
	return False
	
def all_letter_guessed(word):
	for letter in word:
		if (guessed_letters.lower()).find(letter.lower()) == -1:
			return True
	return False
			
play()