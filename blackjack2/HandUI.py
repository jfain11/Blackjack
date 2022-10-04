from BlackjackHand import *
from graphics import *
class HandUI(BlackjackHand):
    _win: GraphWin

    def __init__(self, win: GraphWin, name: str = "", stayValue: int = 21):
        super().__init__(name, stayValue)
        _win = win

    def displayHand(self, point: Point) -> None:
        pass

    def displayName(self, point: Point) -> None:
        pass

