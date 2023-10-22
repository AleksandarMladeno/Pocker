from app_poker.core.hand_calculator import HandCalculator
from app_poker.model.hand import Hand
from app_poker.model.card import Card
from app_poker.model.suit import Suit
from app_poker.config.standard.hand_rank import HandRank
from app_poker.config.standard.card_ranks import card_ranks
from app_poker.model.card_values import (
    ace_card_value,
    king_card_value,
    queen_card_value,
    jack_card_value,
    ten_card_value,
)

hand_calculator = HandCalculator()


def test_calculate_highest_hand_rank_correctly_returns_straight():
    # TODO: implement tests
    assert False
