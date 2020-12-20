"""The tests for word.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the word module
"""
from unittest import TestCase
from unittest.mock import patch

from hanggame.word import *

TEST_WORDS = ['A', 'TestWordOne', '123', '_', 'TestWordTwo']


class TestWord(TestCase):
    @patch.object(Word, 'load_words', return_value=TEST_WORDS)
    def setUp(self, lw) -> None:
        self.word = Word()
        self.word.load_words = lw

    def test_load_words(self):
        """Tests that game has a default 370103 alpha words"""
        # Prepare test
        alpha_words_size = 370103

        # Run test
        words = Word.load_words()

        # Evaluate test
        self.assertEqual(len(words), alpha_words_size)

    def test_word_bank(self):
        # Run test
        result = self.word.word_bank

        # Evaluate test
        self.assertEqual(result, [TEST_WORDS[1], TEST_WORDS[4]])

    def test_unmasked_set(self):
        """Tests that no letter unmasked at the beginning and that returns a set"""
        # Prepare test
        self.word.choose()

        # Run test
        results = self.word.unmasked_set

        # Evaluate test
        self.assertEqual(results, set())

    def test_choose(self):
        """Tests that it chooses a correct word from the list"""
        # Run test
        self.word.choose()

        # Evaluate test
        self.assertIn(self.word.show(), TEST_WORDS)

    def test_is_masked_true(self):
        """Tests that the word correctly report that it is masked"""
        # Prepare test
        self.word.choose()

        # Run test
        result = self.word.is_masked()

        # Evaluate test
        self.assertTrue(result)

    def test_is_masked_false(self):
        """Tests that the word correctly report that it is not masked"""
        # Prepare test
        self.word.choose()

        # Run test
        self.word.show()
        result = self.word.is_masked()

        # Evaluate test
        self.assertFalse(result)

    def test_is_unmasked_false(self):
        """Tests that a masked letter is not reported unmasked"""
        # Prepare test
        letter = 'T'
        self.word.choose()

        # Run test
        result = self.word.is_unmasked(letter)

        # Evaluate test
        self.assertFalse(result)

    def test_is_unmasked_true(self):
        """Tests that an unmasked letter is reported unmasked"""
        # Prepare test
        letter = 'T'
        self.word.choose()

        # Run test
        self.word.unmask(letter)
        result = self.word.is_unmasked(letter)

        # Evaluate test
        self.assertTrue(result)

    def test_show(self):
        """Tests that showing the word then empty it"""
        # Prepare test
        self.word.choose()

        # Run test
        self.word.show()
        w2 = self.word.show()

        # Evaluate test
        self.assertEqual(w2, EMPTY_WORD)

    def test_unmask_worked(self):
        """Test if the a letter from the word could be unmasked and reports it properly"""
        # Prepare test
        letter = 'T'
        self.word.choose()

        # Run test
        worked = self.word.unmask(letter)

        # Evaluate test
        self.assertIn(letter, str(self.word))
        self.assertTrue(worked)

    def test_unmasked_already_unmasked(self):
        """Tests trying to unmask an unmasked letter does not work"""
        # Prepare test
        letter = 'T'
        self.word.choose()

        # Run test
        self.word.unmask(letter)
        worked = self.word.unmask(letter)

        # Evaluate test
        self.assertIn(letter, str(self.word))
        self.assertFalse(worked)

    def test_unmask_failed_not_in_word(self):
        """Tests that unmasking a letter not in word fails"""
        # Prepare test
        letter = 'Z'
        self.word.choose()

        # Run test
        worked = self.word.unmask(letter)

        # Evaluate test
        self.assertNotIn(letter, str(self.word))
        self.assertFalse(worked)
