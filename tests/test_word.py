"""The tests for word.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the word module

File structure
--------------
*constant*
    **DICTIONARY_SIZE**
        The size of the accepted english alpha words dictionary
    **TEST_WORDS_LIST**
        A list of good and wrong words used to conduct tests

"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import patch

from hanggame.word import *

MINIMUM_DICTIONARY_SIZE = 100000
TESTS_WORDS_LIST = ['A', 'TestWordOne', '123', '_', 'TestWordTwo', 'kjfdlksj']


class TestWord(TestCase):
    @patch.object(Word, 'load_words', return_value=TESTS_WORDS_LIST)
    def setUp(self, lw) -> None:
        self.word = Word()
        self.word.load_words = lw

    def test_load_words(self):
        """Tests that a game has DICTIONARY_SIZE alpha words in dictionary"""
        # Prepare test
        alpha_words_size = MINIMUM_DICTIONARY_SIZE

        # Run test
        words = Word.load_words()

        # Evaluate test
        self.assertGreater(len(words), alpha_words_size)

    def test_word_bank(self):
        # Run test
        result = self.word.word_bank

        # Evaluate test
        self.assertEqual(result, [TESTS_WORDS_LIST[1], TESTS_WORDS_LIST[4]])

    def test_unmasked_set(self):
        """Tests that it returns an empty set after the word chosen"""
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
        self.assertIn(self.word.show(), [w.lower() for w in TESTS_WORDS_LIST])

    def test_is_mask_true(self):
        """Tests that the word correctly report that it is masked"""
        # Prepare test
        self.word.choose()

        # Run test
        result = self.word.is_mask()

        # Evaluate test
        self.assertTrue(result)

    def test_is_mask_false(self):
        """Tests that the word correctly report that it is not masked"""
        # Prepare test
        self.word.choose()

        # Run test
        self.word.show()
        result = self.word.is_mask()

        # Evaluate test
        self.assertFalse(result)

    def test_is_masked_true(self):
        """Tests that a masked letter is not reported unmasked"""
        # Prepare test
        letter = 't'
        self.word.choose()

        # Run test
        result = self.word.is_masked(letter)

        # Evaluate test
        self.assertTrue(result)

    def test_is_masked_false(self):
        """Tests that an unmasked letter is reported unmasked"""
        # Prepare test
        letter = 't'
        self.word.choose()

        # Run test
        self.word.unmask(letter)
        result = self.word.is_masked(letter)

        # Evaluate test
        self.assertFalse(result)

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
        """Test the 't' letter could be unmasked and reports it properly"""
        # Prepare test
        letter = 't'
        self.word.choose()

        # Run test
        worked = self.word.unmask(letter)

        # Evaluate test
        self.assertIn(letter, str(self.word))
        self.assertTrue(worked)

    def test_unmasked_already_unmasked(self):
        """Tests trying to unmask an unmasked letter does not work"""
        # Prepare test
        letter = 't'
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
        letter = 'z'
        self.word.choose()

        # Run test
        worked = self.word.unmask(letter)

        # Evaluate test
        self.assertNotIn(letter, str(self.word))
        self.assertFalse(worked)

    def test_available(self):
        # Prepare test
        self.word.choose()

        # Run test
        result = self.word.available

        # Evaluate test
        self.assertEqual(sorted(list(''.join(i18n.ALPHA_LAYOUT))),
                         sorted(result))

    def test_has_vowels_true(self):
        # Run test
        result = self.word.has_vowel(TESTS_WORDS_LIST[1])

        # Evaluate test
        self.assertTrue(result)

    def test_has_vowels_false(self):
        # Run test
        result = self.word.has_vowel(TESTS_WORDS_LIST[5])

        # Evaluate test
        self.assertFalse(result)
