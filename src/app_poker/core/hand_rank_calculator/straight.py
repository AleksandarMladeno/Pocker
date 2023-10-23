from app_poker.core.util.occurrence_counter import count_occurrences
from app_poker.model.card import Card


def is_straight(cards: [Card]):
    """
    Determines if a list of cards is a Poker Straight rank.
    Flow:
        - collect number of times each card appears (i.e. card_value_counts)
        - determine the range between the smallest and highest card's rank.
            axiom: the distance between these is always 4 in a straight.
                    hence max_card_rank_range = 4 in the algorithm.
                    example:
                        2 to 6:
                            6 - 2 = 4
                        3 to 7:
                            7 - 3 = 4
        - if there are no duplicate cards and the axiom above is satisfied then, it is a straight.
            it is so because you have numbers A and B,
                where A is the minimum and B the maximum rank
                    A . . . B
                    A, c₁, c₂, c₃, B
                and there are no duplicate ranks
                    therefore:
                        c₁, c₂, c₃ > A and
                        c₁, c₂, c₃ < B
        - check if it is an ace low straight
            ace_low_straight = ["A", "2", "3", "4", "5"] = [2, 3, 4, 5, 14]
            NB: This is a constant.

    Computational Complexity Analysis:
        N = number of cards
        total asymptotic complexity = O(N)
    """
    max_card_rank_range_for_straight = 4

    def no_duplicate_card_ranks(counts):
        return len(set(counts.values())) == 1

    def check_ace_low_straight(card_ranks):
        ace_low_straight = [2, 3, 4, 5, 14]
        return set(card_ranks) == set(ace_low_straight)

    card_ranks = [card.rank for card in cards]
    card_ranks_counts = count_occurrences(card_ranks)
    card_ranks_range = max(card_ranks) - min(card_ranks)

    if no_duplicate_card_ranks(card_ranks_counts):
        if card_ranks_range == max_card_rank_range_for_straight:
            return True
        else:
            return check_ace_low_straight(card_ranks)
