# Taking Turns

You can validate scrabble boards.  Now it's time to work out how to have your
players take turns, and play the game.

## A bag of letters

At the beginning of the game, initialize a "bag" of letters to match the [letter
frequencies](http://en.wikipedia.org/wiki/Scrabble_letter_distributions) in Scrabble.

Write a function to "draw" a letter from the bag -- it should return the drawn
letter, and afterwards the bag should no longer contain it.

## Making moves

Write a function make_move that takes in a board, a word, a position to start
the word at, and a rack of letters the player has to choose from.  If the move
is valid it outputs the new board and the resulting rack of letters.

To be valid a move has to have two properties:

* It's a valid move with respect to the board (you did this in the last part)
* All the *new* letters on the board for the move were members of the rack (keep
  in mind that if the word has two As in it, the rack has to have two As in it)

## Turns

There are two players in the game.  They take turns.

Each turn:

* Fill the player's rack from the bag of letters
* Display the board and the player's rack. (Remember 
  the last assignment's function to print a board)
* Ask the player to input their move: a position and a word -- do this until 
  they enter a valid move.
* If the player enters a blank move, consider that a "pass"
* When both players pass in a row, end the game

Don't worry about blanks for now.