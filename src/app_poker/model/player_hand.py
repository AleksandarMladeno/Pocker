from app_poker.model.card import Card


class PlayerHand:
    def __init__(self, cards: [Card]) -> None:
        self.hand = cards
