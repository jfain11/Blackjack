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

        # if the value is an integer
        if isinstance(value, int):
            if value > 51:
                raise InvalidCardError
            elif value < 0:
                raise InvalidCardError
            else:
                self.cardNumber = value

        # if the value is a string
        elif isinstance(value, str):
            value.lower()

            # if the string is 3 characters or fewer. ex: "ac", "4s", "10d"
            if len(value) <= 3:

                # extract the face and the suit from the string
                face = str(value[:(len(value) - 1)])
                suit = str(value[-1])

                # try to find the index of the face and suit in the corresponding stored list
                try:
                    faceIndex = self.faceAbbreviations.index(face)
                    suitIndex = self.suitLetters.index(suit)

                # if an index of either cannot be found then raises InvalidCardError
                except:
                    raise InvalidCardError

                # uses the indexes to set the instance variable _cardNumber to the correct integer
                self._cardNumber = faceIndex + (13 * suitIndex)
            else:
                words = value.split(" ")
                face = words[0].capitalize()
                suit = words[2].capitalize()

                # try to find the index of the face and suit in the corresponding stored list
                try:
                    faceIndex = self.faceNames.index(face)
                    suitIndex = self.suitNames.index(suit)

                # if an index of either cannot be found then raises InvalidCardError
                except:
                    raise InvalidCardError

                # uses the indexes to set the instance variable _cardNumber to the correct integer
                self._cardNumber = faceIndex + (13 * suitIndex)





    def __str__(self) -> str:
        """
        :return: name of card using faceNames and suitNames (e.g., "Ten of Clubs")
        """
        faceIndex = self.cardNumber % 13
        suitIndex = self.cardNumber // 13
        return f"{Card.faceNames[faceIndex]} of {Card.suitNames[suitIndex]}"

    def faceName(self) -> str:
        """
        :return: face name for card using faceNames (e.g., "Ten")
        """
        faceIndex = self.cardNumber % 13
        return f"{Card.faceNames[faceIndex]}"

    def suitName(self) -> str:
        """
        :return: suit name for card using suitNames (e.g., "Clubs")
        """
        suitIndex = self.cardNumber // 13
        return f"{Card.suitNames[suitIndex]}"

    def filename(self) -> str:
        """
        :return: image filename for the card

            filename is of the form: ##s.gif
            where ## is a two-digit number (leading 0 if less than 10)
            and s is a letter corresponding to the suit value
            c for clubs, s for spades, h for hearts, d for diamonds

            "03c.gif" (for three of clubs)
        """
        suitNum = self.cardNumber // 13
        faceNum = self.cardNumber % 13
        suits = 'cshd'
        filename = f"{faceNum + 1:>02}{suits[suitNum]}.gif"
        return filename

    def blackjackValue(self) -> int:
        """
        :return: the blackjack value for the card
        for aces, return 11
        for jack, queen, king, return 10
        for all other face values, return the corresponding integer value
        """
        suitNum = self.cardNumber // 13
        if suitNum == 0:
            return 11
        elif suitNum > 9:
            return 10
        else:
            return suitNum

