#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *

# ----------------------------------------------------------------------

class CardTest(unittest.TestCase):

    # ------------------------------------------------------------------

    def testStrAce2(self):
        c = Card("ac")
        self.assertEqual(0, c._cardNumber, f"Card('ac') expected: 0, _cardNumber: {c._cardNumber}")
        c = Card("as")
        self.assertEqual(13, c._cardNumber, f"Card('as') expected: 13, _cardNumber: {c._cardNumber}")
        c = Card("ah")
        self.assertEqual(26, c._cardNumber, f"Card('ah') expected: 26, _cardNumber: {c._cardNumber}")
        c = Card("ad")
        self.assertEqual(39, c._cardNumber, f"Card('ad') expected: 39, _cardNumber: {c._cardNumber}")

    def testStrJack2(self):
        c = Card("jc")
        self.assertEqual(10, c._cardNumber, f"Card('jc') expected: 10, _cardNumber: {c._cardNumber}")
        c = Card("js")
        self.assertEqual(23, c._cardNumber, f"Card('js') expected: 23, _cardNumber: {c._cardNumber}")
        c = Card("jh")
        self.assertEqual(36, c._cardNumber, f"Card('jh') expected: 36, _cardNumber: {c._cardNumber}")
        c = Card("jd")
        self.assertEqual(49, c._cardNumber, f"Card('jd') expected: 49, _cardNumber: {c._cardNumber}")

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
