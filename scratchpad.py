"""
current system:
-playing a whole word is conflated with playing letters that, when combined with letters on the board, form a word
  -- when playing a word, letters are laid down as a group, and the only checks done are that the letters are present in the player's rack
  --when validating the board, all letters that form a contiguous string, uninterrupted by blank squares, are counted as a word

To do:
- Implement:
	- system for playing a combination of letters in combination with letters already played
		- 
	- system for checking if the letters laid down form a legal word
		- one of the validator functions converts each row and column to a list of words. There are 16 rows and 16 columns. columns = 0-7, rows = 8-15. 
		- when a word is played, depending on the orientation, retrieve that row or column as a string, and check to see if the letters you've laid down in combination with adjacent, already-present letters for a word. If so, score it
			- beginning at the position of the starting letter, check each square forwards and backwards for a space. append each letter to a string, stopping at the first empty square. validate and score word if valid.
				- determine if
	Alternative: To play a word, check each letter as it's being played to see if it's in the player's rack OR on the board. If on the rack but not the board, continue and remove letter from rack and place on board. If on the board, continue and do not check or remove if it's on the rack. If it's not on the board or the rack, stop, print that the move is invalid and restart.
		- function to remove letters: takes starting position, word, and board. 

	- scoring:
		- score all words on board as it was before taking turn and, if new board validates, score entire board afterwards.
	- when a word is played using letters on the board:
		- initialize an empty string
		- starting at the starting space, iterate across squares in the direction and for the length of the word.
		- for each square iterated across, add the letter to the string. if no letter, add a space
		- if index of letter in string equals index of letter in word, remove one of letter from word
		- return altered word to remove letters from rack, return 

Taking a turn:
- print board
- print letter rack
- prompt for word to play
- prompt for starting position
- prompt for orientation
- make move using previous three
 - make a temporary copy of the board to modify
 - unpack starting position into a row, column coordinate
- validate board/move
	- check if letters for word are either on the letter rack or on the board in the correct positions before move was played
	- validate board
	- if board validates
		- remove appropriate letters from rack
		- score word:
#		  - score board prior to word being played
#		  	- add up all previous scores from both players
#		  - score board after move
		  	- get all words from board prior to move
		  	- get all words from board after move
		  	- determine the squares the letters in the new words are on
		  	  - create a tuple of the word and its starting position
		  	  	- create two lists, each containing the rows and columns as strings for each board
		  	  	- for each item in each list, if the 
"""

on_board = []
for i in range(len(word)):
	if orientation == VERTICAL:
		if 'letter' in board[row][column+i]:
			on_board.append(board[row][column+i]['letter'])
		else:
			on_board.append('.')
	elif orientation == HORIZONTAL:
		if 'letter' in board[row+i][column]:
			on_board.append(board[row+i][column]['letter'])
		else:
			on_board.append('.')
	if word[i] == on_board[i]:
		letter_rack.remove(word[i])

def letters_are_present(word, board, letter_rack, position, orientation):
    row, column = position
    if orientation == HORIZONTAL:
    	for i in range(len(word)):
	    	if not (letter in letter_rack and word.count(letter) <= letter_rack.count(letter)) or letter in board[row+i][column]:
	        	return False
    elif orientation == VERTICAL:
        for i in range(len(word)):
	        if not (letter in letter_rack and word.count(letter) <= letter_rack.count(letter)) or letter in board[row][column+i]:
	        	return False
    return True


def remove_letters(word, board, letter_rack, position, orientation):
 	on_board = []
 	row, column = position
	for i in range(len(word)):
		if orientation == VERTICAL:
			if 'letter' in board[row][column+i]:
				on_board.append(board[row][column+i]['letter'])
			else:
				on_board.append('.')
		elif orientation == HORIZONTAL:
			if 'letter' in board[row+i][column]:
				on_board.append(board[row+i][column]['letter'])
			else:
				on_board.append('.')
	if word[i] != on_board[i]:
		letter_rack.remove(word[i])

"""
current issue:
- scoring: how to score all new words created from letters laid down in a single turn
	- method 1: score board twice, once as it appears before the turn, and once as it appears after. the score for that turn is the difference of the two scores. 
		- at the end of the turn, for all squares with a letter in them, remove score modifier.
		-
	- method 2: check adjacent letters to see what new words are being formed
		- for the first square, check to see if there are any squares before it with letters in them
		- for each square, if orientation is vertical, check horizontally adjacent squares for letters. if orientation is horizontal, check each vertically adjacent squares for letters.
		- for the last square, check to see if there are any squares after it with letters in them
		- one recursive function to check vertically adjacent squares, one for horizontally adjacent
	- method 3: hybrid of method 1 & method 2. 
		- retrieve all rows and columns that intersect with that row both before and after played move. 
		- retrieve all words from intersecting rows and columns both before and after move. make two lists, one of words before, one of words after
		- if word in list one 

"""

def score_move(board_before, board_after, score_list):
	rows_and_columns = validator.get_rows_and_columns_as_strings(board)

def check_horizontally_adjacent_squares(board, position):
	row, column = position
	if 'letter' in board[row][column+1]:

def check_vertically_adjacent_squares(board, position):
	row, column = position
	if 'letter' in board[row+1][column]:

def assign_multipliers(board):
	for i in range(1, 6, 4):
		for j in range(1, 6, 4):
			board[i][j]['letter_mult'] = 3
			board[i][14-j]['letter_mult'] = 3
			board[14-i][j]['letter_mult'] = 3
			board[14-i][14-j]['letter_mult'] = 3
	for i in range(1, 14, 12):
		for j in range(1, 14, 12):
			del board[i][j]['letter_mult']
	for i in range(0, 15, 7):
		board[0][i]['word_mult'] = 3
		board[7][i]['word_mult'] = 3
		board[14][i]['word_mult'] = 3
	for i in range(1, 5):
		board[i][i]['word_mult'] = 2
		board[i][14-i]['word_mult'] = 2
		board[i+9][5-i]['word_mult'] = 2
		board[i+9][9+i]['word_mult'] = 2
	board[7][7]['word_mult'] = 2
	double_letters = [(0, 3), (2, 6), (3, 0), (6, 2), (6, 6), (7, 3), (3, 7)]
	for row, column in double_letters:
	   board[row][column]['letter_mult'] = 2
	   board[row][14-column]['letter_mult'] = 2
	   board[14-row][column]['letter_mult'] = 2
	   board[14-row][14-column]['letter_mult'] = 2

listy = [(7, 7), (7, 8), (7, 9), (7, 10), (6, 7), (5, 7), (4, 7), (4, 8), (4, 9), (5, 9), (6, 9)]