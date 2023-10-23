"""
    A map from card value to card rank.
    This is used to determine Poker hand rank in a HandRank.
    i.e. when hands have the same hand rank, the card ranks are used to rank them.

    NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
"""

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
