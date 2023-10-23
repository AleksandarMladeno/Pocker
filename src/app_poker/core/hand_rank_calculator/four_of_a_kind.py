from app_poker.model.card import Card
from collections import defaultdict


def is_four_of_a_kind(cards: [Card]):
    """
    Determines if a list of cards is a Poker Four of a Kind rank.
    Computational Complexity Analysis:
        N = number of hand cards
        total asymptotic complexity = O(N)
    """
    card_ranks = [card.rank for card in cards]
    card_ranks_counts = defaultdict(lambda: 0)
    for card_rank in card_ranks:
        card_ranks_counts[card_rank] += 1
    expected_card_counts_sorted = [1, 4]

    return expected_card_counts_sorted == sorted(card_ranks_counts.values())
