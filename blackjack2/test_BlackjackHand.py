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

    # tests the constructor for every integer in range 0-51

    def testInit(self):
        h = BlackjackHand()
        self.assertEqual(h.score(), 0)

    def testReset(self):
        pass

    def testCanGetCard(self):
        pass

    def testAddCard(self):
        h = BlackjackHand()

        h.addCard(Card("4c"))
        self.assertEqual(h.score(), 4)

        h.addCard(Card("9s"))
        self.assertEqual(h.score(), 13)

        h.addCard(Card("ac"))
        self.assertEqual(h.score(), 14)

        h.addCard(Card("ah"))
        self.assertEqual(h.score(), 15)

        h.addCard(Card("6c"))
        self.assertEqual(h.score(), 21)

        h.addCard(Card("9d"))
        self.assertEqual(h.score(), 30)


    def testScore(self):
        pass

    def testBusted(self):
        pass

    def testStr(self):
        pass

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
