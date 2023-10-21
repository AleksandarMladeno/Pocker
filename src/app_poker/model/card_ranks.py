"""
    A map from card value to card rank.
    This is used to determine Poker hand rank in a HandRank.
    i.e. when hands have the same hand rank, the card ranks are used to rank them.

    NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
"""

card_ranks = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "10": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}
