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
    def testHand(self):
        hand = BlackjackHand("jacob")
        print(hand.score())
        hand.addCard(Card("4c"))
        print(hand.score())
        hand.addCard(Card("ac"))
        print(hand.score())
        hand.addCard(Card("6c"))
        print(hand.score())
        hand.addCard(Card("ac"))
        print(hand.score())



# ----------------------------------------------------------------------

def main():
    unittest.main()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
