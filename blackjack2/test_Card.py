# Jacob Fain
# CS261

#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *

# ----------------------------------------------------------------------

class CardTest(unittest.TestCase):

    # ------------------------------------------------------------------

    # tests the constructor for every integer in range 0-51
    def testAllInts(self):
        for i in range(52):
            c = Card(i)
            self.assertEqual(i, c._cardNumber, f"Card({i}) expected: {i}, _cardNumber: {c._cardNumber}" )

    # tests the constructor for all possible three character string combinations
    def testAllShortStr(self):
        nums = [0, 13, 26, 39]
        for i in range(len(Card.faceAbbreviations)):
            for x in range(len(Card.suitLetters)):
                result = Card.faceAbbreviations[i] + Card.suitLetters[x]
                c = Card(result)
                self.assertEqual(nums[x], c._cardNumber, f"Card({result}) expected: {nums[x]}, _cardNumber: {c._cardNumber}")
                nums[x] += 1

    # tests the constructor for all possible three word combinations
    def testAllLongStr(self):
        nums = [0, 13, 26, 39]
        for i in range(len(Card.faceNames)):
            for x in range(len(Card.suitNames)):
                result = Card.faceNames[i] + " of " + Card.suitNames[x]
                c = Card(result)
                self.assertEqual(nums[x], c._cardNumber, f"Card({result}) expected: {nums[x]}, _cardNumber: {c._cardNumber}")
                nums[x] += 1

    # tests to ensure the constructor is able to handle any variation of capitalization
    def testCapitalization(self):
        i = "AC"
        c = Card(i)
        self.assertEqual(0, c._cardNumber, f"Card({i}) expected: {0}, _cardNumber: {c._cardNumber}")

        i = "10H"
        c = Card(i)
        self.assertEqual(35, c._cardNumber, f"Card({i}) expected: {35}, _cardNumber: {c._cardNumber}")

        i = "Kd"
        c = Card(i)
        self.assertEqual(51, c._cardNumber, f"Card({i}) expected: {51}, _cardNumber: {c._cardNumber}")

    # tests to ensure InvalidCardError is raised when and integer outside the 0-51 range is entered
    def testInvalidIntRaises(self):
        with self.assertRaises(InvalidCardError):
            c = Card(52)
        with self.assertRaises(InvalidCardError):
            c = Card(-1)

    # tests to ensure InvalidCardError is raised when and invalid 2-3 character string is entered
    def testInvalidStr2or3Raises(self):
        with self.assertRaises(InvalidCardError):
            c = Card("ca")
        with self.assertRaises(InvalidCardError):
            c = Card("14c")

    # tests to ensure InvalidCardError is raised when and invalid long string is entered
    def testInvalidStrRaises(self):
        with self.assertRaises(InvalidCardError):
            c = Card("Ace of Club")

        with self.assertRaises(InvalidCardError):
            c = Card("as4da6s2fs")

    # tests to ensure the __str__ method returns the correct name of the card
    def testStr(self):
        c = Card(1)
        self.assertEqual("Two of Clubs", str(c), f"Card({1}) expected: Two of Clubs, Card Name: {str(c)}")

        c = Card(35)
        self.assertEqual("Ten of Hearts", str(c), f"Card({35}) expected: Ten of Hearts, Card Name: {str(c)}")

    # tests to ensure the faceName method returns the correct face name
    def testFaceName(self):
        c = Card(2)
        self.assertEqual("Three", c.faceName(), f"Card({2}) expected: Three, Face Name: {c.faceName()}")

        c = Card(36)
        self.assertEqual("Jack", c.faceName(), f"Card({36}) expected: Jack, Face Name: {c.faceName()}")

    # test to ensure the suitName method returns the correct suit name
    def testSuitName(self):
        c = Card(2)
        self.assertEqual("Clubs", c.suitName(), f"Card({2}) expected: Clubs, Suit Name: {c.suitName()}")

        c = Card(36)
        self.assertEqual("Hearts", c.suitName(), f"Card({36}) expected: Hearts, Suit Name: {c.suitName()}")

    # tests to ensure the filename method returns the correct filename
    def testFilename(self):
        c = Card(3)
        self.assertEqual("04c.gif", c.filename(), f"Card({3}) expected: 04c.gif, Filename: {c.filename()}")

        c = Card(37)
        self.assertEqual("12h.gif", c.filename(), f"Card({37}) expected: 12h.gif, Filename: {c.filename()}")

    # tests to ensure the blackJackValue method returns the correct value
    def testBlackJackValue(self):
        c = Card(0)
        self.assertEqual(11, c.blackjackValue(), f"Card({0}) expected: {11}, Blackjack Value: {c.blackjackValue()}")

        c = Card(5)
        self.assertEqual(6, c.blackjackValue(), f"Card({6}) expected: {6}, Blackjack Value: {c.blackjackValue()}")

        c = Card(12)
        self.assertEqual(10, c.blackjackValue(), f"Card({10}) expected: {10}, Blackjack Value: {c.blackjackValue()}")
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------

def main():
    unittest.main()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
