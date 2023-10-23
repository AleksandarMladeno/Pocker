from app_poker.config.high_game.card_ranks import card_ranks
from app_poker.config.high_game.hand_rank import HandRank
from app_poker.core.hand_rank_calculator.calculator import HandRankCalculator
from app_poker.model.card import Card
from app_poker.model.card_values import (
    six_card_value,
    five_card_value,
    nine_card_value,
    eight_card_value,
    seven_card_value,
)
from app_poker.model.hand import Hand
from app_poker.model.suit import Suit

hand_calculator = HandRankCalculator()


def test_calculate_highest_hand_rank_returns_straight_flush():
    suit = Suit.Clubs
    cards = [
        Card(nine_card_value, suit, card_ranks[nine_card_value]),
        Card(eight_card_value, suit, card_ranks[eight_card_value]),
        Card(seven_card_value, suit, card_ranks[seven_card_value]),
        Card(six_card_value, suit, card_ranks[six_card_value]),
        Card(five_card_value, suit, card_ranks[five_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.STRAIGHT_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)
