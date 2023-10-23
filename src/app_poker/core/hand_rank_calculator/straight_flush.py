from app_poker.model.card import Card
from app_poker.core.hand_rank_calculator.flush import is_flush
from app_poker.core.hand_rank_calculator.straight import is_straight


def is_straight_flush(cards: [Card]):
    """
    Determines if a list of cards is a Poker Straight Flush rank.
    Computational Complexity Analysis:
    is_straight:
        N = number of cards
        R = number of royals

        R = 5, only 5 royal cards i.e. A,K,Q,J,10

        O(N) + O(R) = O(N) + O(5) = O(N) + O(1) = O(N)

    is_flush: O(N)

    total asymptotic complexity:
        is_flush + are_all_cards_royal
        O(N) + O(N) = O(2N) = O(N).
            NB: Constants are removed from asymptotic upper-bound runtime as they don't affect it.
    """

    return is_flush(cards) and is_straight(cards)
