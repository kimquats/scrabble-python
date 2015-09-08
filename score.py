import validator
import board

def get_words_from_played_lines(board, position, orientation, word):
    """
    

    Parameters:
    board - a scrabble board in the array-of-arrays format.

    """
    lines = []
    row, column = position
    if orientation = 'horizontal':
    	string_columns = []
	    for i in range(len(word)):
	    	for j in range(len(board)):
		    	current_column = ''
		        if 'letter' in  board[row+j][column+i]:
		        current_column.append(board[row+j][column+i]['letter'])
		    lines.append(current_column)
		played_row = ''
		for i in range(len(word)):
			played_row.append(board[row][column+i]['letter'])
		lines.append(played_row)
	elif orientation = 'vertical':
	    for i in range(len(word)):
	    	for j in range(len(board)):
		    	current_row = ''
		        if 'letter' in  board[row+i][column+j]:
		        current_row.append(board[row+i][column+j]['letter'])
		    lines.append(current_row)
		played_column = ''
		for i in range(len(word)):
			played_column.append(board[row][column+i]['letter'])
		lines.append(played_row)
	return validator.get_all_words(lines)

def get_new_words(words_from_last_turn, words_from_current_turn):
	"""
	Takes in two lists, one containing words on the played lines from the previous turn, and one containing words on the played lines from the current turn, and determines the new words that were created in the current turn.
	"""
	new_words = []
	for word in words_from_current_turn:
		if word not in words_from_last_turn:
			new_words.append(word)
	return new_words

