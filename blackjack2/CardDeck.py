import Card

class CardDeck:
    _cards: list

    def __init__(self):
        pass

    def freshDeck(self):
        """
        creates a fresh un-shuffled 52 card deck
        :return: None
        """
        pass

    def shuffle(self):
        """
        shuffles the deck of cards
        :return: None
        """
        pass

    def dealOne(self) -> Card:
        """
        deals one off the top of the deck and removes it from the deck
        :return: the card off the top of the deck; in position 0 of the cards list
        """
        pass