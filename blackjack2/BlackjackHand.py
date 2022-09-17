import Card

class BlackjackHand:
    _score: int
    _hand: list

    def __init__(self):
        pass

    def __updateScore(self):
        """
        calculates the total score of the cards within the hand and updates the instance variable _score
        is called whenever a new card is inserted
        :return: None
        """
        pass

    def insertCard(self, card: Card):
        """
        inserts a card into the hand
        :param card: the card to insert into the hand
        :return: None
        """
        pass

    def clearHand(self):
        """
        removes all the cards from the hand
        :return: None
        """
        pass

    def score(self) -> int:
        """
        :return: the combined blackjack score of all the cards in the hand
        """
        pass

    def __len__(self) -> int:
        """
        :return: the length of the hand (number of cards in the hand)
        """
        pass

    def __eq__(self, other) -> bool:
        """
        compares if the blackjack score of two blackjackHand objects is equal
        :param other: a different blackjackHand object
        :return: true if they are equal and false if not
        """
        pass

    def __gt__(self, other) -> bool:
        """
        compares if one blackjackHand object's score is greater than another blackjackHand object's score
        :param other: a different blackjackHand object
        :return:
        """
        pass


    def __lt__(self, other) -> bool:
        """
        compares if one blackjackHand object's score is less than another blackjackHand object's score
        :param other: a different blackjackHand object
        :return:
        """
        pass




    