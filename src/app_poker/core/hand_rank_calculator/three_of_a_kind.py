from app_poker.core.util.occurrence_counter import count_occurrences
from app_poker.model.card import Card


def is_three_of_a_kind(cards: [Card]):
    """
    Determines if a list of cards is a Poker Three of a Kind rank.
    Computational Complexity Analysis:
        N = number of hand cards
        total asymptotic complexity = O(N)
    """
    card_ranks = [card.rank for card in cards]
    card_ranks_counts = count_occurrences(card_ranks)
    expected_card_counts_sorted = [1, 1, 3]
    return expected_card_counts_sorted == sorted(card_ranks_counts.values())
