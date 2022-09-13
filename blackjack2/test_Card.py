#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *

# ----------------------------------------------------------------------

class CardTest(unittest.TestCase):
    faceAbbreviations = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k')
    suitLetters = ('c', 's', 'h', 'd')
    faceNames = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                 "Jack", "Queen", "King")
    suitNames = ("Clubs", "Spades", "Hearts", "Diamonds")
    # ------------------------------------------------------------------

    def testAllInts(self):
        for i in range(52):
            c = Card(i)
            self.assertEqual(i, c._cardNumber, f"Card({i}) expected: {i}, _cardNumber: {c._cardNumber}" )

    def testAllShortStr(self):
        nums = [0, 13, 26, 39]
        for i in range(len(Card.faceAbbreviations)):
            for x in range(len(Card.suitLetters)):
                result = Card.faceAbbreviations[i] + Card.suitLetters[x]
                c = Card(result)
                self.assertEqual(nums[x], c._cardNumber, f"Card({result}) expected: {nums[x]}, _cardNumber: {c._cardNumber}")
                nums[x] += 1

    def testAllLongStr(self):
        nums = [0, 13, 26, 39]
        for i in range(len(Card.faceNames)):
            for x in range(len(Card.suitNames)):
                result = Card.faceNames[i] + " of " + Card.suitNames[x]
                c = Card(result)
                self.assertEqual(nums[x], c._cardNumber, f"Card({result}) expected: {nums[x]}, _cardNumber: {c._cardNumber}")
                nums[x] += 1


    def testInvalidIntRaises(self):
        with self.assertRaises(InvalidCardError):
            c = Card(52)
        with self.assertRaises(InvalidCardError):
            c = Card(-1)

    def testInvalidStr2or3Raises(self):
        with self.assertRaises(InvalidCardError):
            c = Card("ca")
        with self.assertRaises(InvalidCardError):
            c = Card("14c")

    def testInvalidStrRaises(self):
        with self.assertRaises(InvalidCardError):
            c = Card("Ace of Club")

    # ------------------------------------------------------------------


# ----------------------------------------------------------------------

def main():
    unittest.main()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
