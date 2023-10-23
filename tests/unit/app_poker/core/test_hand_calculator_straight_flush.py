from app_poker.config.standard.card_ranks import card_ranks
from app_poker.config.standard.hand_rank import HandRank
from app_poker.core.hand_rank_calculator.calculator import HandRankCalculator
from app_poker.model.card import Card
from app_poker.model.card_values import (
    ace_card_value,
    jack_card_value,
    king_card_value,
    queen_card_value,
    ten_card_value,
    six_card_value,
    five_card_value,
    four_card_value,
    three_card_value,
    two_card_value,
)
from app_poker.model.hand import Hand
from app_poker.model.suit import Suit

hand_calculator = HandRankCalculator()


def test_calculate_highest_hand_rank_returns_straight_flush():
    suit = Suit.Clubs
    cards = [
        Card(ace_card_value, suit, card_ranks[six_card_value]),
        Card(king_card_value, suit, card_ranks[five_card_value]),
        Card(queen_card_value, suit, card_ranks[four_card_value]),
        Card(jack_card_value, suit, card_ranks[three_card_value]),
        Card(ten_card_value, suit, card_ranks[two_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.STRAIGHT_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)
