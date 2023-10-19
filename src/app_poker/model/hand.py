from card import Card

from app_poker.model.hand_rank import HandRank


class Hand:
    # TODO: decide where to add the 5 cards requirement validation
    def __init__(self, cards: [Card]) -> None:
        self.hand = cards

    def rank(self) -> [HandRank]:
        """
        see analysis for the algorithm for how to calculate a hand's ranks
        from patterns of cards.
        """
        pass

    def rank_within_rank(self) -> int:
        """
        see analysis for the algorithm for how to calculate a hand's rank
        within its rank using the hand's card ranks.
        """
        pass
