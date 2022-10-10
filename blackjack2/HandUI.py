# Jacob Fain
# CS261

from BlackjackHand import *
from graphics import *
from typing import List


class HandUI(BlackjackHand):

    # stores the window
    _win: GraphWin

    # stores a list of the card objects in the hand
    _cards: List[Card]

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

    def drawHand(self, point: Point) -> None:
        """

        :param point: the point at which to draw the hand
        :return:
        """
        pass

    # draws the label
    def drawLabel(self, point: Point) -> None:
        """

        :param point: the point at which to draw the label
        :return: None
        """
        pass

    def addCard(self, card: Card) -> None:
        """
        the same as blackjackHand's addCard except also stores the card object in the _cards instance variable
        :param card:
        :return: None
        """
        pass

    def reset(self) -> None:
        """
        the same as blackjackHand's reset except also undraws the card objects, removes them from _cards, and resets the score in the label
        :return: None
        """
        pass

