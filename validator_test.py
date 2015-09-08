import board
import samples
import validator
import unittest

def validate_str_board(s):
    """ A helper function to validate a string board """
    return validator.validate(board.read_board(s))

class TestValidator(unittest.TestCase):

    def test_valid(self):
        """ Some test cases for boards that are valid """
        self.assertEqual(validate_str_board(samples.SAMPLE_BOARD), True)

    def test_invalid_words(self):
        """ Some test cases where there's just an invalid word """
        self.assertEqual(validate_str_board(samples.SAMPLE_BAD1), False)
        self.assertEqual(validate_str_board(samples.SAMPLE_BAD2), False)

    def test_floating_words(self):
        """ Some test cases where there are floating words """
        self.assertEqual(validate_str_board(samples.SAMPLE_BAD3), False)
        self.assertEqual(validate_str_board(samples.SAMPLE_BAD4), False)


# What does this do? ;)
if __name__ == '__main__':
    unittest.main()
