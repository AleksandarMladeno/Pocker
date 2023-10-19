"""
    NB: Not necessary for current objective. added to paint a full picture, to design a system that would 
    be extensible for modelling and solving Poker problems.
    
    A map from card name to card rank.
    This map is configuration of a Poker rule-set.

    If we were building a generic app_poker, for different variations of poker.
    We would instantiate it from a database, loaded when a request to determine
    a winner, from a set of hands, for a specific poker rule-set came in.

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
