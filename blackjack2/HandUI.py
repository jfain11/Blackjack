# Jacob Fain
# CS261

from BlackjackHand import *
from graphics import *
from typing import List


class HandUI(BlackjackHand):
    # stores the window
    _win: GraphWin

    # stores a list of the image objects currently being drawn in the window
    _drawnCards: List[Image]

    # the text object which will display the player name & score
    _label: Text

    def __init__(self, win: GraphWin, name: str = "", stayValue: int = 21):
        """
        :param win: the window
        :param name: a name for the hand
        :param stayValue: values below stayValue have canGetCard return True
        """
        pass

    def drawCard(self, card: Card, point: Point) -> None:
        """
        draws the card and also adds it to the _drawnCards list.
        :param card: the card object to be drawn
        :param point: the point at which to draw the card
        :return: None

        pre: already have called addCard with the cardObject so that it is also in the hand
        """
        pass

    def drawLabel(self, point: Point) -> None:
        """
        draws the label
        :param point: the point at which to draw the label
        :return: None
        """
        pass

    def undrawCard(self, pos: int) -> None:
        """
        undraws a card from _drawnCards
        :param pos: the position of the image in the _drawnCards list (first card added is 0)
        :return:
        """
        pass

    def undrawLabel(self) -> None:
        """
        undraws the label
        :return: None
        """
        pass

    def reset(self) -> None:
        """
        the same as blackjackHand's reset except also undraws all the card objects, removes them from _cards, and resets the score in the label
        :return: None
        """
        pass

