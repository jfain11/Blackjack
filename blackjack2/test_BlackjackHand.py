# Jacob Fain
# CS261

#!/usr/bin/env python3

import sys
import unittest

sys.path.insert(0, '..')
from Card import *

# ----------------------------------------------------------------------

class BlackjackHandTest(unittest.TestCase):

    # ------------------------------------------------------------------

    # tests the constructor for every integer in range 0-51
    def testHand(self):
        for i in range(52):
            c = Card(i)
            self.assertEqual(i, c._cardNumber, f"Card({i}) expected: {i}, _cardNumber: {c._cardNumber}" )


# ----------------------------------------------------------------------

def main():
    unittest.main()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
