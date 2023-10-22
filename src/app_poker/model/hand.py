from app_poker.model.card import Card


class Hand:
    def __init__(self, cards: [Card]) -> None:
        self.hand = cards
