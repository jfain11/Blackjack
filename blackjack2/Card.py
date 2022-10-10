#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Card.py
# Jacob Fain
# 04/09/2022
# ----------------------------------------------------------------------

from __future__ import annotations


# custom Exception to raise if Card constructor is passed invalid data
class InvalidCardError(Exception):
    pass

# ----------------------------------------------------------------------

class Card:

    """
    stores a card from a standard playing card deck of 52 cards
    """

    # one or two character face abbreviation for card
    faceAbbreviations = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k')

    # one-character letter for each suit (Clubs, Spaces, Hearts, Diamonds)
    suitLetters = ('c', 's', 'h', 'd')

    # full name of each face
    faceNames = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                  "Jack", "Queen", "King")

    # full name of each suit
    suitNames = ("Clubs", "Spades", "Hearts", "Diamonds")

    # instance variable from 0 to 51 (see constructor documentation string)
    _cardNumber: int

    # ------------------------------------------------------------------

    def __init__(self, value: int | str):
        """
        creates a card from int or str
        if value is an int
            0-12 are the Ace-King of clubs
            13-25 are the Ace-King of spades
            26-38 are the Ace-King of hearts
            39-51 are the Ace-King of diamonds
        elif value is a str
            the str can be of length 2 or 3 with the last character being the suit letter (see suitLetters)
            and the first character or two being face abbreviation (see faceAbbreviations)
                "ac" (for ace of clubs), "10D" (ten of diamonds)
                face and suit can be either upper or lower case
            or the string can be of the form "ace of clubs" (see class variables faceNames and suitNames)
            allow the str to have any capitalization
        raises InvalidCardError if the int is out of range or the str is not valid

        :param value: int (0-51) or a str as described above
        """
        if isinstance(value, int):
            if value < 0 or value > 51:
                raise InvalidCardError(f"invalid int for Card initialization (must be 0 to 51): {value}")
            self._cardNumber = value

        elif isinstance(value, str):
            value = value.strip()
            # version that is 2 or 3 characters such as ad or 10c
            if len(value) <= 3:
                # suit is last character
                suit = value[-1].lower()
                # face is everything except last character (first character or first two characters)
                face = value[:-1].lower()

                # get indices from class variables
                try:
                    suitNumber = Card.suitLetters.index(suit)
                    faceNumber = Card.faceAbbreviations.index(face)
                # raise error if failed
                except ValueError:
                    raise InvalidCardError(f'invalid string for Card initialization: "{value}"') from None

            # longer str that should be of form "Ace of Clubs"
            else:
                # break into list such as ["Ace", "of", "Clubs"]
                s = value.split()
                try:
                    # convert to lower case and then capitalize first letter
                    face = s[0].lower().capitalize()
                    suit = s[2].lower().capitalize()
                    # get indices from class variables
                    suitNumber = Card.suitNames.index(suit)
                    faceNumber = Card.faceNames.index(face)
                # raise error if failed
                except (ValueError, IndexError):
                    raise InvalidCardError(f'invalid string for Card initialization: "{value}"') from None

            # 13 cards per suit and then offset for face
            self._cardNumber = suitNumber * 13 + faceNumber

        else:
            raise InvalidCardError("invalid type: must pass int or str")

    def __str__(self) -> str:
        """
        :return: name of card using faceNames and suitNames (e.g., "Ten of Clubs")
        """
        return f"{self.faceName()} of {self.suitName()}"

    def __eq__(self, other: Card) -> bool:
        """
        :param other: Card to compare
        :return: True if both cards are the same, False otherwise
        """
        return self._cardNumber == other._cardNumber

    def __ne__(self, other: Card) -> bool:
        """
        :param other: Card to compare
        :return: True if both cards are not the same, False otherwise
        """
        return self._cardNumber != other._cardNumber

    def faceName(self) -> str:
        """
        :return: face name for card using faceNames (e.g., "Ten")
        """
        # 13 cards per suit so get face offset
        faceNum = self._cardNumber % 13
        return f"{Card.faceNames[faceNum]}"

    def suitName(self) -> str:
        """
        :return: suit name for card using suitNames (e.g., "Clubs")
        """
        # 13 cards per suit
        suitNum = self._cardNumber // 13
        return f"{Card.suitNames[suitNum]}"

    def filename(self) -> str:
        """
        :return: image filename for the card

            filename is of the form: ##s.gif
            where ## is a two-digit number (leading 0 if less than 10)
            and s is a letter corresponding to the suit value
            c for clubs, s for spades, h for hearts, d for diamonds
            "01c.gif" (for ace of clubs)
            "02c.gif" (for two of clubs)
            "03c.gif" (for three of clubs)
            and so on
        """

        faceNum = self._cardNumber % 13
        suitNum = self._cardNumber // 13
        # right justify faceNum+1 in two spaces with leading zero, followed by suit letter and .gif
        return f"{faceNum+1:0>2}{Card.suitLetters[suitNum]}.gif"

    def blackjackValue(self) -> int:
        """
        :return: the blackjack value for the card
        for aces, return 11
        for jack, queen, king, return 10
        for all other face values, return the corresponding integer value
        """
        # face value from 1 to 13
        value = self._cardNumber % 13 + 1
        # 1 is ace
        if value == 1:
            value = 11
        # anything more than 10, is jack, queen, or king so those are worth 10
        elif value > 10:
            value = 10
        return value

# ----------------------------------------------------------------------


