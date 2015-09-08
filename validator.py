import board
import samples
import copy

def validate(d):
    """
    Returns True if the board is a valid Scrabble board, False if not.

    Parameters:
    d - a board in the array-of-arrays format.
    """
    scratchboard = copy.deepcopy(d)
    return are_squares_connected(scratchboard) and check_all_words(scratchboard)

def are_squares_connected(d):
    """
    For a given board, checks to see if each played letter is connected to the center square through other played squares. Returns True if squares are connected, False if there are any 'dangling' letters.

    Parameters:
    d - a board in the array-of-arrays format.
    """
    mark_connected_squares(d, 7, 7)
    for x in range(len(d)):
        for y in range(len(d[x])):
            if 'letter' in d[x][y] and 'connected' not in d[x][y]:
                return False
    return True


def check_all_words(d):
    """
    Returns true if all words on the board are legal words (present in the game's dictionary), false if there are any illegal words.

    Parameters:
    d - a board in the array-of-arrays format.

    """
    strings = get_rows_and_columns_as_strings(d)
    played_words = get_all_words(strings)
    with open('word_list.txt', 'r') as f:
        wordlist = f.read()
        wordlist = wordlist.splitlines()
    for word in played_words:
        word = word.upper()
        if word not in wordlist:
            return False
    return True

def get_rows_and_columns_as_strings(d):
    """
    For a given input board, return a list containing strings of all rows and all columns.

    Parameters:
    d - a board in the array-of-arrays format.

    """

    strings = []
    for x in range(len(d)):
        row = ''
        for y in range(len(d[x])):
            if 'letter' in d[x][y]:
                row += d[x][y]['letter']
            else:
                row += '.'
        strings.append(row)
    for y in range(len(d)):
        column = ''
        for x in range(len(d[y])):
            if 'letter' in d[x][y]:
                column += d[x][y]['letter']
            else:
                column += '.'
        strings.append(column)
    return strings

def get_all_words(strings):
    """
    For a list containing each row and column of the chosen board represented as a string, convert each column and each row into a list of words, defined as more than one letter in adjacent positions.

    Parameters:

    strings - a list containing each row and column of the board represented as a string, with unplayed squares represented as '.'

    Returns a list of words. Since words in scrabble must be more than one letter, the output strings will only include strings with two or more letters in a row.

    """
    words = []
    for string in range(len(strings)):
        current_string = strings[string].split('.')
        for word in current_string:
          if word.isalpha() and len(word) > 1:
              words.append(word)
    return words

    

def mark_connected_squares(d, row, column):
    """
    For a given board, marks all squares with letters in them that are connected to the center square as connected.

    Parameters:
    d - a board in the array-of-arrays format.
    row - the index for the row of the square to check and mark.
    column - the index for the column of the square to check and mark.

    """
    if 'letter' in d[row][column] and 'connected' not in d[row][column]:
        d[row][column]['connected'] = True
        for offset in range(-1, 2):
           try:
             mark_connected_squares(d, row+offset, column)
           except IndexError:
             pass 
           try:
             mark_connected_squares(d, row, column+offset)
           except IndexError:
             pass

def print_board_with_statuses(board):
    """
    Print a board so that each row is on its own line.
    An empty space is represented by ' '
    A played letter is represented by that letter
    Bonus modifiers for a played letter are indicated by a 2w, 3l, etc next to the letter.
    If the played letter is connected to the center square, it is followed by '*'

    """
    for row in board:
        for square in row:
            if 'letter' in square and 'bonus' not in square and 'connected' not in square:
                print square['letter'],
            elif 'letter' in square and 'connected' in square:
                print square['letter'] + '*',
            elif 'letter' in square and 'bonus' in square and 'connected' in square:
                print square['letter'] + square['bonus'] + '*',
            else:
                print '.',
        print