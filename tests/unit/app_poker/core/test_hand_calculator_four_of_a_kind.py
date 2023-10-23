from app_poker.config.high_game.card_ranks import card_ranks
from app_poker.config.high_game.hand_rank import HandRank
from app_poker.core.hand_rank_calculator.calculator import HandRankCalculator
from app_poker.model.card import Card
from app_poker.model.card_values import (
    queen_card_value,
    five_card_value,
)
from app_poker.model.hand import Hand
from app_poker.model.suit import Suit

hand_calculator = HandRankCalculator()


def test_calculate_highest_hand_rank_correctly_returns_four_of_a_kind():
    cards = [
        Card(queen_card_value, Suit.Clubs, card_ranks[queen_card_value]),
        Card(five_card_value, Suit.Diamonds, card_ranks[five_card_value]),
        Card(five_card_value, Suit.Hearts, card_ranks[five_card_value]),
        Card(five_card_value, Suit.Spades, card_ranks[five_card_value]),
        Card(five_card_value, Suit.Clubs, card_ranks[five_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.FOUR_OF_A_KIND
    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)
