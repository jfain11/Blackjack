#!/usr/bin/env python3

# ----------------------------------------------------------------------
# BlackjackHand.py
# Jacob Fain
# 04/10/2022
# ----------------------------------------------------------------------

from __future__ import annotations

from Card import Card


class BlackjackHand:

    # name for the hand
    _name: str

    # value at which the hand stops getting cards
    _stayValue: int

    # total value of the hand
    _total: int

    # True if the hand has an ace counted as 11
    _hasAce11: bool

    # ------------------------------------------------------------------

    def __init__(self, name: str = "", stayValue: int = 21):
        """
        :param name: a name for the hand
        :param stayValue: values below stayValue have canGetCard return True
        """
        self._name = name
        self._stayValue = stayValue
        self._total = 0
        self._hasAce11 = False

    def reset(self) -> None:
        """
        resets state to an empty hand
        :return: None
        """
        self._total = 0
        self._hasAce11 = False

    def canGetCard(self) -> bool:
        """
        :return: True if total < the stay value, False otherwise
        """
        return self._total < self._stayValue

    def addCard(self, card: Card) -> None:
        """
        adds card to the hand
        :param card: Card to add
        :return: None
        """
        value = card.blackjackValue()
        # handle Ace as 1 or 11
        if value == 11:
            # if already have over 10, this card should be counted as 1 to avoid busting
            if self._total > 10:
                value = 1
            # we have an ace that is counted as 11
            else:
                self._hasAce11 = True

        # if adding this card would bust and we have an ace as 11
        if self._total + value > 21 and self._hasAce11:
            self._total += value - 10
            self._hasAce11 = False
        else:
            self._total += value

    def score(self) -> int:
        """
        :return: total value of the hand
        """
        return self._total

    def busted(self) -> bool:
        """
        :return: True if hand total > 21, False otherwise
        """
        return self._total > 21

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
        name = self._name.strip()
        if name != "":
            name = name + ":"

        if self._total > 21:
            return f"{name} busted".strip()
        else:
            return f"{name} {self._total}".strip()

    # ------------------------------------------------------------------

    def __lt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self, otherwise False
        """
        if self.busted() and other.busted():
            return False
        elif other.busted():
            return False
        elif self.busted():
            return True
        return self._total < other._total

    def __eq__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if both hands the same (a tie), False otherwise
        """
        if self.busted() and other.busted():
            return True
        if self.busted() or other.busted():
            return False
        else:
            return self._total == other._total

    def __ne__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if one hand beats the other, False otherwise
        """
        return not self == other

    def __le__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if other beats self or a tie, False otherwise
        """
        return self < other or self == other

    def __gt__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other, False otherwise
        """
        return not self <= other

    def __ge__(self, other: BlackjackHand) -> bool:
        """
        :param other: BlackjackHand to compare
        :return: True if self beats other or a tie, False otherwise
        """
        return not self < other

# ----------------------------------------------------------------------

