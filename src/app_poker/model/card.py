from dataclasses import dataclass
from app_poker.model.suit import Suit


@dataclass(frozen=True)
class Card:
    """
    value: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    suit: Spades, Hearts, Diamonds, Clubs.
    rank: looked up before instantiation in card_rank configuration

    In the context of Poker, each card has a rank.
    If we were modelling playing cards independent of a game,
    the rank property wouldn't be there.
    """

    value: str
    suit: Suit
    rank: int
