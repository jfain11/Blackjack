# Jacob Fain
# CS261

class Card:
    _suit: str
    _value: int

    def __init__(self, _value: int, _suit: str):
        """
        :param _value: the integer value of the card
        :param _suit: string representation
        """
        pass

    def filename(self) -> str:
        """
        generates the filename of the image that corresponds to the card
        :return: the filename of the image as a string
        """
        pass

    def cardValue(self) -> int:
        """
        returns card value
        :return: the value of the card as an integer
        """
        pass

    def cardSuit(self) -> str:
        """
        returns card suit
        :return: returns the suit of the card as a string. ex: "c"
        """
        pass