Your goal is to make the validator_test.py pass all three tests by
completing the validate() function in validator.py.

There's a word list in `word_list.txt`.  It's a file full of all-caps words, all
of which are valid scrabble words.

You're going to be writing some code like:

    with open("word_list.txt") as f:
       #do something to read f.

to read in the word list.

## Hints:

* Break the problem down into small pieces.  There's not too much code to
write here, but just a lot of things to think about.

* There are two cases that a board can be invalid.

  - the words on the board are not legal Scrabble words (i.e. in the word list)

  - the words are not connected to the start square.


* Think about writing helper functions.  Specifically, the two ways that the
board can be invalid can be their own helper functions.  Here are some
suggestions of helper functions you might want to have:

  * get_rows_and_columns_as_strings(board)
  * get_all_words(board)
  * check_all_words(board)
  * are_squares_connected(board)
  * mark_connected_squares(board)

Please do email `info@transcodesf.org` if you run into any questions.  This is
the most independent you've been in a homework yet, and it is not easy stuff.