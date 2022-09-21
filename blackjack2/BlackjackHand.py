from __future__ import annotations

from Card import Card

class BlackjackHand:
    # name for the hand
    _name: str

    # value at which the hand stops getting cards
    _stayValue: int

    # list of cards
    _cards = list[Card]

    # ------------------------------------------------------------------

    def __init__(self, name: str = "", stayValue: int = 21):
        """
        :param name: a name for the hand
        :param stayValue: values below stayValue have canGetCard return True
        """
        self._name = name
        self._stayValue = stayValue
        self._cards = []

    def reset(self) -> None:
        """
        resets state to an empty hand
        :return: None
        """
        self._cards = []

    def canGetCard(self) -> bool:
        """
        :return: True if total < the stay value, False otherwise
        """
        if self.score() < self._stayValue:
            return True
        return False


    def addCard(self, card: Card) -> None:
        """
        adds card to the hand
        :param card: Card to add
        :return: None
        """
        self._cards.append(card)

    def score(self) -> int:
        """
        :return: total value of the hand
        """
        score = 0
        for c in self._cards:
            value = c.blackjackValue()
            if value == 11:
                if score + value > 21:
                    score += 1
                else:
                    score += value
            else:
                score += value

        return score




    def busted(self) -> bool:
        """
        :return: True if hand total > 21, False otherwise
        """
        if self.score() > 21:
            return True
        return False


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
            pass
        else:
            pass

    # ------------------------------------------------------------------

    def __lt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self, otherwise False
        """
        if self == other:
            return False
        elif self.busted():
            return True
        elif self.score() < other.score():
            return True
        return False


    def __eq__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if both hands the same (a tie), False otherwise
        """
        if self.busted() or other.busted():
            if self.busted() and other.busted():
                return True
            return False

        if self.score() == other.score():
            return True
        return False


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
        elif self < other:
            return True
        else:
            return False


    def __gt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other, False otherwise
        """
        if other < self:
            return True
        else:
            return False

    def __ge__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other or a tie, False otherwise
        """
        if self == other:
            return True
        elif self > other:
            return True
        else:
            return False

# ----------------------------------------------------------------------

