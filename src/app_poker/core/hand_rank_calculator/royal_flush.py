from app_poker.model.card import Card
from app_poker.model.card_values import (
    ace_card_value,
    king_card_value,
    queen_card_value,
    jack_card_value,
    ten_card_value,
)
from app_poker.core.hand_rank_calculator.flush import is_flush


def is_royal_flush(cards: [Card]):
    """
    Determines if a list of cards is a Poker Royal Flush rank.
    Computational Complexity Analysis:
    are_all_cards_royal:
        N = number of cards
        R = number of royals

        R = 5, only 5 royal cards i.e. A,K,Q,J,10

        O(N) + O(R) = O(N) + O(5) = O(N) + O(1) = O(N)

    is_flush: O(N)

    total asymptotic complexity:
        is_flush + are_all_cards_royal
        O(N) + O(N) = O(2N) = O(N). Constants are removed from asymptotic upper-bound runtime as they don't affect it.
    """

    def are_all_cards_royal(cards):
        royal_cards = [
            ace_card_value,
            king_card_value,
            queen_card_value,
            jack_card_value,
            ten_card_value,
        ]
        non_royal = [card for card in cards if card.value not in royal_cards]
        return len(non_royal) == 0

    return is_flush(cards) and are_all_cards_royal(cards)
