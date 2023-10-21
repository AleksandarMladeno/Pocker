class Card:
    """
    value: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    suit: Spades, Hearts, Diamonds, Clubs.
    rank: looked up before instantiation in card_rank configuration

    In the context of Poker, each card has a rank.
    If we were modelling playing cards independent of a game,
    the rank property wouldn't be there.
    """

    def __init__(self, value, suit, rank) -> None:
        self.value = value
        self.suit = suit
        self.rank = rank
