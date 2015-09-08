import copy
import validator
import random
import math

#Get an array initialized, 15x15
def make_board():
    return [[{} for i in range(15)] for j in range(15)]
    #    row = []
    #    for j in range(15):
    #        row.append({})
    #    board.append(row)
    #return board

def assign_multipliers(board):
    """
    Modifies a given board to include the score multipliers for each square, in accordance with the official rules of Scrabble.
    """
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

def initialize_letters():
    """
    Initialize the bag of letters that are available to play, as per official scrabble rules. Returns a list containing all playable letters in the correct amounts.
    """
    letter_counts = 'KJXQZ' + 'BCMPFHVWY'*2 + 'G'*3 + 'LSUD'*4 + 'NRT'*6 +'O'*8 + 'AI'*9 + 'E'*12
    letters = []
    for letter in letter_counts:
        letters.append(letter)
    return letters

def initialize_rack(letter_bag):
    """
    Initializes a player's starting letter rack. Returns a list of 7 letters and removes them from the letter bag.
    """
    #letter_rack = []
    #for i in range(7):
    #    letter_rack.append(draw_letter(letter_bag))
    #return letter_rack
    return [draw_letter(letter_bag) for i in range(7)]

def initialize_players(letter_bag):
    """
    Returns a dictionary containing an entry for each play
    """
    players = {}
    for i in range(2):
       player = players['player' + str(i+1)] = []
       player.append([])
       player.append(initialize_rack(letter_bag))
    return players

def initialize_game():
    """
    Initializes the board, the bag of letters, the players, and the number of passes.
    """
    board = make_board()
    board = assign_multipliers(board)
    letter_bag = initialize_letters()
    players = initialize_players(letter_bag)
    pass_count = 0
    return board, letter_bag, players, pass_count

def draw_letter(letter_bag):
    """
    Chooses a letter randomly from the letter bag, modifies the letter bag in place to remove the chosen letter, then returns the letter.
    """
    letter = random.choice(letter_bag)
    letter_bag.remove(letter)
    return letter


def score_word(word, score_list):
    with open('letter_values.txt', 'r') as v:
        value_list = []
        for line in v:
            value_list.append(line.rstrip('\n'))
    values = {}
    value_list2 = []
    for line in value_list:
        value_list2.append(line.split(' '))
    for line in value_list2:
        values[line[1]] = line[0]
    sorted_values = sorted(values.keys())
    score = []
    for letter in word:
      for val in sorted_values:
        if letter in values[val]:
          score.append(int(val))
    score_list.append(int(math.fsum(score)))


def print_board(board):
    """
    Print a board so that each row is on its own line.
    An empty space is represented by '.'
    A played letter is represented by that letter
    """
    for row in board:
        for square in row:
            if 'letter' in square:
                print square['letter'],
            else:
                print '.',
        print

def print_board_multipliers(board):
    """
    Print a board so that each row is on its own line.
    An empty space is represented by '.'
    The multiplier present on a square is represented by a number
    """
    for row in board:
        for square in row:
            if 'letter_mult' in square:
                print str(square['letter_mult']) + 'l',
            elif 'word_mult' in square:
                print str(square['word_mult']) + 'w',
            else:
                print '.',
        print

def letters_are_present(board, word, letter_rack, position, orientation):
    """
    For a given word to be played on a given board, checks to see if the letters are available in the letter rack or at the correct position on the board.
    """
    row, column = position
    if orientation == HORIZONTAL:
        for i in range(len(word)):
            if not ((word[i] in letter_rack and word.count(word[i]) <= letter_rack.count(word[i])) or word[i] in board[row][column+i]):
                return False
            else:
                return True
    elif orientation == VERTICAL:
        for i in range(len(word)):
            if not ((word[i] in letter_rack and word.count(word[i]) <= letter_rack.count(word[i])) or word[i] in board[row+i][column]):
                return False
            else:
                return True
    else:
        pass


def play_letter(letter, board, position):
    """
    Takes the given letter and board, and checks if the position on the board
    can accept that letter.

    If so, modifies the board to have that letter on it.

    If not, raises an error.
    """
    row, column = position
    square = board[row][column]
    if 'letter' in square:
        if letter != square['letter']:
            raise Exception('You tried to play %s, but the board contained %s' %
                        (letter, square['letter']))
            pass
    else:
        square['letter'] = letter

HORIZONTAL, VERTICAL = ("horizontal", "vertical")

def play_word(board, word, position, orientation):
    """
    board: Board to place the word on.  See above.

    word: the string word to play

    position: a tuple of coordinates (row, column) for the initial letter of the
    word to play.

    orientation: either "horizontal" or "vertical"

    raises an error if the coordinates for the word don't fall within the board.

    raises an error if the word conflicts with letters already on the board.

    returns a new board with the new word on it, as well as all the words
    already on the board.
    """
    #make the new board
    board = copy.deepcopy(board)
    #for every letter in the word to add
    #   find its coordinates
    #   check to see if it conflicts
    #   if the square is empty, play on it
    #   If the square is occupied, report any conflicts, but otherwise leave alone
    row, column = position
    for l in word:
        play_letter(l, board, (row, column))
        if orientation == HORIZONTAL:
            column += 1
        elif orientation == VERTICAL:
            row += 1
    return board

def read_board(str_board):
    """Takes in a string in the form of a grid of letters
    Returns a board in the format described above."""
    board = make_board();
    lines = str_board.splitlines()
    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter.isalpha():
                play_letter(letter, board, (row, col))
    return board

def validate_board(board):
    if validator.validate(board) == True:
        return True
    else:
        return False

#def score_move(board_before_move, board_after_move, score_list):
#    """
#    Takes in a given board before a move is made and after, scores that move, and appends the resulting score to a player's score list.
#    """
#    words = 

def make_move(board, score_list, word, position, letter_rack, letter_bag, orientation):
    """
    Takes in a board, a word, a position to start the word at, the orientation of the word to play, and a rack of letters the player has to choose from and plays a word at that position.  If the move is valid, it returns the new board and mod.

    Parameters:

    board - The board for the game currently being played, formatted as a list of lists.

    word - The word the current player is attempting to play, in a string in capital letters.

    position - A tuple containing the coordinates for the starting square for the word the player is attempting to play.

    letter_rack - A list of letters available to the player to play their current word.

    letter_bag - A list of letters available to all players as they play the letters currently in their rack.

    orientation - One of two possible orientations for the word being played, either 'horizontal' or 'vertical'.
    """
    temp_board = copy.deepcopy(board)
    row, column = position
    #for letter in word:
    #    if not (letter in letter_rack and word.count(letter) <= letter_rack.count(letter)) or letter in board[row][column]:
    #        print "You do not have the proper letters in your rack or on the board to play this word."
    #            return board
    #    if orientation == HORIZONTAL:
    #        column += 1
    #    elif orientation == VERTICAL:
    #        row += 1
    if letters_are_present(board, word, position, orientation):
        temp_board = play_word(temp_board, word, position, orientation)
    if validator.validate(temp_board):
        for letter in word:
            letter_rack.remove(letter)
        for i in range(len(word)):
            letter_rack.append(draw_letter(letter_bag))
        board = temp_board
    else:
        retry_word = raw_input("You have made an illegal move. Try again ")
        make_move(board, score_list, retry_word, position, letter_rack, letter_bag, orientation)
    return board

def take_turn(board, player, letter_bag, pass_count):
    """
    Fills a player's rack of letters (if possible), displays the board and that player's rack of tiles, asks the player to input a move until they input a valid move, and, if no move is entered, the turn ends with the player passing.
    """
    while len(player[1]) < 7:
        player[1][1].append(draw_letter(letter_bag))
    print_board(board)
    for letter in player[1][1]:
        print letter,
    word = raw_input('Enter a word to play. ').upper()
    position = (input('Enter the starting row to play your word. '), input('Enter the starting column to play your word. '))
    orientation = raw_input('Orientation to play this word in? (vertical or horizontal)').lower()
    if len(word) == 0:
        pass_count += 1
        return board, pass_count
    else:
       temp_board = make_move(board, player[0], word, position, player[1], letter_bag, orientation)
       return temp_board, pass_count

def play_game():
    """
    Starts a game and plays until both players pass in a row.
    """
    board, letter_bag, players, pass_count = initialize_game()
    player_list = sorted(players.keys())
    while pass_count < 2:
        for i in range(2):
            board, pass_count = take_turn(board, players[player_list[i]], letter_bag, pass_count)
    print 'The game has ended. Scores are as follows:'
    for player in player_list:
        print player + ' ' + str(sum(players[player][0]))
    if sum(players[player_list[0]][0]) > sum(players[player_list[1]][0]):
        print 'Player 1 wins!'
    elif sum(players[player_list[1]][0]) > sum(players[player_list[0]][0]):
        print 'Player 2 wins!'
    else:
        print "It's a tie!"


#board, letter_bag, players, pass_count = initialize_game()
#while pass_count < 2:
#    take_turn(players['player1'][1], board, letter_bag, pass_count)
#    take_turn(players['player2'][1], board, letter_bag, pass_count)
#print board
#print "Player 1 scored " + str(int(math.fsum(players['player1'][0]))) + ' points.'
#print "Player 2 scored " + str(int(math.fsum(players['player2'][0]))) + ' points.'
#if math.fsum(players['player1'][0]) > math.fsum(players['player2'][0]):
#    print 'Player 1 wins!'
#elif math.fsum(players['player1'][0]) < math.fsum(players['player2'][0]):
#    print 'Player 2 wins!'
#elif math.fsum(players['player1'][0]) == math.fsum(players['player2'][0]):
#    print "It's a tie!"