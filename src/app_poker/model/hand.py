from dataclasses import dataclass
from app_poker.model.card import Card


@dataclass(frozen=True)
class Hand:
    cards: [Card]
