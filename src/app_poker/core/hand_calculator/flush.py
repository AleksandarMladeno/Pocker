from app_poker.model.card import Card


def is_flush(cards: [Card]):
    suits = [card.suit for card in cards]
    return len(set(suits)) == 1
