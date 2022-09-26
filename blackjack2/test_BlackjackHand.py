# Jacob Fain
# CS261

#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *
from BlackjackHand import *

# ----------------------------------------------------------------------

class BlackjackHandTest(unittest.TestCase):

    # ------------------------------------------------------------------

    # tests the reset() method of the BlackjackHand class
    def testReset(self):
        h = BlackjackHand()
        h.reset()
        self.assertEqual(0, h.score())

        h.addCard(Card("7h"))
        h.reset()
        self.assertEqual(0, h.score())

        h.addCard(Card("7h"))
        h.addCard(Card("3c"))
        h.addCard(Card("kd"))
        h.addCard(Card("8s"))
        h.reset()
        self.assertEqual(0, h.score())

    # tests the canGetCard() method of the BlackjackHand class
    def testCanGetCard(self):
        h = BlackjackHand()
        self.assertTrue(h.canGetCard())

        h.addCard(Card("kh"))
        self.assertTrue(h.canGetCard())

        h.addCard(Card("qh"))
        self.assertTrue(h.canGetCard())

        h.addCard(Card("5d"))
        self.assertFalse(h.canGetCard())

        h.addCard(Card("9d"))
        self.assertFalse(h.canGetCard())

    # tests the addCard() method of the BlackjackHand class
    def testAddCard(self):
        h = BlackjackHand()

        h.addCard(Card("4c"))
        self.assertEqual(4, h.score())

        h.addCard(Card("9s"))
        self.assertEqual(13, h.score())

        h.addCard(Card("ac"))
        self.assertEqual(14, h.score())

        h.addCard(Card("ah"))
        self.assertEqual(15, h.score())

        h.addCard(Card("6c"))
        self.assertEqual(21, h.score())

        h.addCard(Card("6c"))
        self.assertEqual(27, h.score())

    # tests the score() method of the BlackjackHand class
    def testScore(self):
        h = BlackjackHand()
        self.assertEqual(0, h.score())

        h.addCard(Card("ac"))
        self.assertEqual(11, h.score())

        h.addCard(Card("7h"))
        self.assertEqual(18, h.score())

        h.addCard(Card("6c"))
        self.assertEqual(14, h.score())

        h.addCard(Card("6d"))
        self.assertEqual(20, h.score())

        h.addCard(Card("ac"))
        self.assertEqual(21, h.score())

        h.addCard(Card("kc"))
        self.assertEqual(31, h.score())

    # tests the busted() method of the BlackjackHand class
    def testBusted(self):
        h = BlackjackHand()
        self.assertFalse(h.busted())

        h.addCard(Card("kh"))
        self.assertFalse(h.busted())

        h.addCard(Card("qh"))
        self.assertFalse(h.busted())

        h.addCard(Card("5d"))
        self.assertTrue(h.busted())

        h.addCard(Card("9d"))
        self.assertTrue(h.busted())

    # tests the __str__() method of the BlackjackHand class
    def testStr(self):

        # if _name is empty and _total is 5, it just returns "5"
        h = BlackjackHand()
        h.addCard(Card("5c"))
        self.assertEqual("5", str(h))

        # if _name is empty and the player has busted, it just returns "busted"
        h = BlackjackHand()
        h.addCard(Card("9c"))
        h.addCard(Card("9c"))
        h.addCard(Card("9c"))
        self.assertEqual("busted", str(h))

        # if _name is "Player 1" and _total is 5, it returns "Player 1: 5"
        h = BlackjackHand("Player 1")
        h.addCard(Card("5c"))
        self.assertEqual("Player 1: 5", str(h))

        # if _name is "Player 1" and the player has busted, it returns "Player 1: busted"
        h = BlackjackHand("Player 1")
        h.addCard(Card("9c"))
        h.addCard(Card("9c"))
        h.addCard(Card("9c"))
        self.assertEqual("Player 1: busted", str(h))

    # tests the __lt__() method of the BlackjackHand class
    def testLT(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertFalse(h1 < h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertTrue(h1 < h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertFalse(h1 < h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 < h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertFalse(h1 < h2)

    # tests the __eq__() method of the BlackjackHand class
    def testEQ(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertTrue(h1 == h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertFalse(h1 == h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertFalse(h1 == h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertFalse(h1 == h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 == h2)

    # tests the __ne__() method of the BlackjackHand class
    def testNE(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertFalse(h1 != h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertTrue(h1 != h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertTrue(h1 != h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 != h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertFalse(h1 != h2)

    # tests the __le__() method of the BlackjackHand class
    def testLE(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertTrue(h1 <= h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertTrue(h1 <= h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertFalse(h1 <= h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 <= h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 <= h2)

    # tests the __gt__() method of the BlackjackHand class
    def testGT(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertFalse(h1 > h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertFalse(h1 > h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertTrue(h1 > h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 > h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertFalse(h1 > h2)

    # tests the __ ge__() method of the BlackjackHand class
    def testGE(self):
        h1 = BlackjackHand()
        h2 = BlackjackHand()

        # equal score
        h1.addCard(Card("4c"))
        h2.addCard(Card("4c"))
        self.assertTrue(h1 >= h2)

        # h1 < h2
        h1.addCard(Card("2c"))
        h2.addCard(Card("3c"))
        self.assertFalse(h1 >= h2)

        # h1 > h2
        h1.addCard(Card("9c"))
        h2.addCard(Card("7c"))
        self.assertTrue(h1 >= h2)

        # h2 busts
        h1.addCard(Card("2c"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 >= h2)

        # both bust
        h1.addCard(Card("kc"))
        h2.addCard(Card("kc"))
        self.assertTrue(h1 >= h2)


# ----------------------------------------------------------------------

def main():
    unittest.main()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
