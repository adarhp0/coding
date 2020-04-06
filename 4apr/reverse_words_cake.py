import unittest


def reverse_words(message):
    left_index  = 0
    right_index = len(message) - 1
    while left_index < right_index:
        # Swap characters
        message[left_index], message[right_index] = message[right_index], message[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1
    las=-1
    el=0
    for i in range(len(message)+1):
        if i==len(message) or message[i]==' ':
            left_index  = las+1
            right_index = i-1
            las=i
            while left_index < right_index:
            # Swap characters
                message[left_index], message[right_index] = message[right_index], message[left_index]
            # Move towards middle
                left_index  += 1
                right_index -= 1
    """
    left_index  = las+1
    right_index = len(message)-1
    while left_index < right_index:
            # Swap characters
        message[left_index], message[right_index] = message[right_index], message[left_index]
            # Move towards middle
        left_index  += 1
        right_index -= 1
    """
    
    
    """
    # Decode the message by reversing the words
    las=-1
    for i in range(len(message)):
        if message[i]==' ':
            message[las+1:i]=message[las+1:i:-1]
            las=i"""
    


















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)