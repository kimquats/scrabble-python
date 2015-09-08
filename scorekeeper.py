import sys

def score_file_to_dict():
    """
    Opens the file containing players' scores and enters the information contained within
    into a dictionary of (player): (list of player's scores each round) pairs. Returns a tuple containing this dictionary as well as an alphabetical list of the players.

    Exits if there is a problem opening the file containing players' scores.
    """
    try:
      with open('scores.txt', 'r') as f:
        scores = f.read()
      scores = scores.split()
    except IOError:
      print "There was an error opening or reading scores.txt. Creating a new file."
      with open('scores.txt', 'w') as g:
        pass
      scores = []
    d = {}
    for i in range(len(scores)):
        if scores[i].isalpha():
            player = scores[i]
            d[player] = []
        else:
            d[player].append(int(scores[i]))
    p = sorted(d.keys())
    return d, p

def print_scores(scores, players):
    """
    Given a tuple containing a dictionary of players' scores and a list of players, prints each player and their current score.

    Parameters:

    scores - A dictionary containing players and their scores from each round.

    players - A list of players.
    """
    print "Total points per player:"
    for i in range(len(players)):
      print players[i], ':', sum(scores[players[i]])

def ask_for_scores(scores, players):
  """
  Prompts the user for each player's score this round and updates a dictionary of their scores.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.
  """
  for i in range(len(players)):
      score = ''
      while not score.isdigit():
          try:
            print "How many points did", players[i], "score?",
            score = raw_input()
            scores[players[i]].append(int(score))
          except ValueError:
            print "The score you enter must be an integer. Try again."
  print_scores(scores, players)

def write_to_scores_file(scores, players):
  """
  Writes a dictionary containing each player's score to a text file 'scores.txt'. If the file cannot be accessed, exits the program.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.  

  """
  try:
    with open('scores.txt', 'w') as f:
      for player in players:
        f.write(player)
        f.write("\n")
        for i in range(len(scores[player])):
          f.write(str(scores[player][i]))
          f.write("\n")
  except IOError:
    print "There was an error writing to scores.txt."
    

def check_number_of_rounds(scores, players):
  """
  Checks to see if each player has played the same number of rounds, and prints an error message if they have not.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.

  """
  rounds = []
  for player in players:
    rounds.append(len(scores[player]))
    print player + ' has played ' + str(len(scores[player])) + ' rounds.'
  for i in range(len(rounds)-1):
    if rounds[i] != rounds[i+1]:
      print "Not all players have played the same number of rounds."
      break
  print "All players have played the same number of rounds."

def print_average_scores(scores, players):
  """
  Prints each player's average score per rounds as a floating-point number.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.

  """
  average_scores = []
  for player in players:
    average_scores.append(float(sum(scores[player]))/len(scores[player]))
  for i in range(len(average_scores)):
    print players[i] + "'s average score per round is " + str(average_scores[i])

def sort_scores_and_players(scores, players):
  """
  For a dictionary of players' scores and a sorted list of players, returns a list of tuples containing each player's total score and their name, sorted by score.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.
  """
  score_list = []
  for player in players:
    score_list.append(sum(scores[player]))
  player_scores = zip(score_list, players)
  player_scores.sort()
  player_scores.reverse()
  return player_scores

def display_winning_player(scores, players):
  """
  Prints out the name of the winning player and their score.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.

  """
  player_scores = sort_scores_and_players(scores, players)
  print player_scores[0][1] + ' is in the lead with ' + str(player_scores[0][0]) + ' points.'

def print_sorted_players_and_scores(scores, players):
  """
  Prints out each player's name and score, sorted from highest score to lowest score.

  Parameters:

  scores - A dictionary containing players and their scores from each round.

  players - A list of players.

  """
  player_scores = sort_scores_and_players(scores, players)
  for i in range(len(player_scores)):
    print player_scores[i][1] + ':' + str(player_scores[i][0])


#scores, players = score_file_to_dict()
#print_scores(scores, players)
#ask_for_scores(scores, players)
#write_to_scores_file(scores, players)
