from app_poker.model.card import Card
from app_poker.model.card_values import (
    ace_card_value,
    king_card_value,
    queen_card_value,
    jack_card_value,
    ten_card_value,
)
from app_poker.core.hand_calculator.flush import is_flush


def is_royal_flush(cards: [Card]):
    """
    Computational Complexity Analysis:
    all_cards_are_royal:
        N = number of royals
        C = number of hand cards

        C = 5, since we are using a 5 card hand
        N = 5, only 5 royal cards i.e. A,K,Q,J,10

        O(N) + O(C)
    is_flush:
        C = number of hand cards
        O(C)
    total asymptotic complexity:
        O(N) + O(C) + O(C)
        O(N) + O(2C)
        O(N) + O(C), constants are removed from asymptotic upper-bound runtime as they don't affect it.
        C is constant, i.e. 5 or 7
        therefore: asymptotic complexity = O(N)
                   which is linear, and that is good.
        it is effectively O(1), because the number of royal cards is constant(i.e. 5)
            which is very good.
    """

    def all_cards_are_royal():
        royal_cards = [
            ace_card_value,
            king_card_value,
            queen_card_value,
            jack_card_value,
            ten_card_value,
        ]
        non_royal = [card for card in cards if card not in royal_cards]
        return len(non_royal) > 0

    return is_flush(cards) and all_cards_are_royal()
