# Jacob Fain
# CS261

from __future__ import annotations
from Card import Card
from typing import List

class BlackjackHand:

    # name for the hand
    _name: str

    # value at which the hand stops getting cards
    _stayValue: int

    # list of cards
    _cards: List[Card]

    # ------------------------------------------------------------------

    def __init__(self, name: str = "", stayValue: int = 21):
        """
        :param name: a name for the hand
        :param stayValue: values below stayValue have canGetCard return True
        """
        # initializes the instance variables
        self._name = name
        self._stayValue = stayValue
        self._cards = []

    def reset(self) -> None:
        """
        resets state to an empty hand
        :return: None
        """
        # sets _cards to an empty list
        self._cards = []

    def canGetCard(self) -> bool:
        """
        :return: True if total < the stay value, False otherwise
        """
        # if score is less than stay value returns True
        return self.score() < self._stayValue

    def addCard(self, card: Card) -> None:
        """
        adds card to the hand
        :param card: Card to add
        :return: None
        """
        # appends the new card onto the end of _cards
        self._cards.append(card)

    def score(self) -> int:
        """
        :return: total value of the hand
        """
        # initializes accumulators
        aceCount = 0
        score = 0

        # loops through the hand and totals the score
        # counts the number of aces in the hand
        for c in self._cards:
            value = c.blackjackValue()

            # counts the aces in the hand
            if value == 11:
                aceCount += 1

            # totals the score of all the cards
            score += value

        # adjusts the score of the aces if the score is greater than 21
        if score > 21:
            for i in range(aceCount):
                score -= 10
                if score < 22:
                    break

        # returns the total blackjack score of the hand
        return score

    def busted(self) -> bool:
        """
        :return: True if hand total > 21, False otherwise
        """
        # if score is greater than 21 then return True
        if self.score() > 21:
            return True
        return False

    # ------------------------------------------------------------------
    # overloaded operators

    def __str__(self) -> str:
        """
        if the player has a name (_name is not the empty string), the return string contains
        the player's name followed by a colon followed by a space and then the score
        if the player has busted, the string "busted" is used instead of the numeric score
        examples:
        if _name is empty and _total is 12, it just returns "12"
        if _name is empty and the player has busted, it just returns "busted"
        if _name is "Player 1" and _total is 12, it returns "Player 1: 12"
        if _name is "Player 1" and the player has busted, it returns "Player 1: busted"
        :return: string as described above
        """

        if self._name == "":

            # if busted with no name
            if self.busted():
                return "busted"
            # if not busted with no name
            else:
                return str(self.score())

        else:
            # if busted with a name
            if self.busted():
                return f"{self._name}: busted"
            # if not busted with a name
            else:
                return f"{self._name}: {self.score()}"

    def __lt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self, otherwise False
        """
        if self == other:
            return False
        elif self.busted():
            return True
        return self.score() < other.score()

    def __eq__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if both hands the same (a tie), False otherwise
        """
        if self.busted() or other.busted():
            return self.busted() and other.busted()

        return self.score() == other.score()

    def __ne__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if one hand beats the other, False otherwise
        """
        if self == other:
            return False
        else:
            return True

    def __le__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self or a tie, False otherwise
        """
        if self == other:
            return True
        return self < other

    def __gt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other, False otherwise
        """

        return other < self

    def __ge__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other or a tie, False otherwise
        """
        if self == other:
            return True
        return self > other

# ----------------------------------------------------------------------

