from app_poker.model.card import Card


def is_flush(cards: [Card]):
    """
    Determines if a list of cards is a Poker Flush rank.
    Computational Complexity Analysis:
        N = number of hand cards
        total asymptotic complexity = O(N)
    """
    suits = [card.suit for card in cards]
    return len(set(suits)) == 1
