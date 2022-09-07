#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *

# ----------------------------------------------------------------------

class CardTest(unittest.TestCase):
    faceAbbreviations = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k')
    suitLetters = ('c', 's', 'h', 'd')
    # ------------------------------------------------------------------


    def testAllStr(self):
        nums = [0, 13, 26, 39]
        for i in range(len(self.faceAbbreviations)):
            for x in range(len(self.suitLetters)):
                result = self.faceAbbreviations[i] + self.suitLetters[x]
                c = Card(result)
                self.assertEqual(nums[x], c._cardNumber, f"Card({result}) expected: {nums[x]}, _cardNumber: {c._cardNumber}")
                nums[x] += 1

    # test capitalization

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
