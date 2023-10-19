class Card:
    """
    TODO: reconsider the name of the `name` property. for now its fine so it covers 1-10 and A-J.
       
    name: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    suit: Spades, Hearts, Diamonds, Clubs.
    rank: looked up before instantiation in card_rank configuration

    In the context of Poker, each card has a rank.
    If we were modelling playing cards independent of a game,
    the rank property wouldn't be there.
    """

    def __init__(self, name, suit, rank) -> None:
        self.name = name
        self.suit = suit
        self.rank = rank
