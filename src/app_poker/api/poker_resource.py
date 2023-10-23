import logging
from flask import Blueprint, Response, request
from app_poker.config.high_game.hand_rank import HandRank
from app_poker.config.high_game.card_ranks import card_ranks
from app_poker.model.hand import Hand
from app_poker.model.card import Card
from app_poker.core.hand_rank_calculator.calculator import HandRankCalculator
from logging import log

hand_rank_calculator = HandRankCalculator()
api_poker = Blueprint("api_poker", __name__)


@api_poker.route("/hand/highest-rank", methods=["POST"])
def highest_rank() -> Response:
    """
    returns highest hand rank possible for input cards.
    input: cards from user.
            example:
                [
                    {
                        value: 2
                        suit: C
                    },
                    {
                        value: A
                        suit: S
                    },
                    {
                        value: 5
                        suit: D
                    },
                    {
                        value: 4
                        suit: H
                    },
                    {
                        value: J
                        suit: C
                    },

                ]
    output: highest Poker hand rank that can be obtained using the input cards.

    """
    # 1. TODO: parse input
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        value_key = "value"
        suit_key = "suit"
        player_hand = request.json
        log(logging.INFO, f"Processing user request: request:{player_hand}")

        # 2. TODO: validate input
        """
        validations:
            - fail if hand does not have 5 cards, 422
            - validate cards:
                card value value
                card suit value
            ...
        """
        for card in player_hand:
            if value_key not in card.keys() or suit_key not in card.keys():
                return "Incorrectly formed request", 422

        hand = Hand(
            [
                Card(card[value_key], card[suit_key], card_ranks[card[value_key]])
                for card in player_hand
            ]
        )

        result = hand_rank_calculator.calculate_highest_hand_rank(hand)
        log(logging.INFO, "Successfully processed user request.")
        return {"highest_rank": result.name}, 200

        # 4. TODO: graceful error handling: https://flask.palletsprojects.com/en/2.3.x/errorhandling/
    else:
        log(logging.INFO, "Failed to process user request.")
        return "Content-Type not supported!", 415


@api_poker.route("/hand/ranks", methods=["POST"])
def retrieve_possible_ranks() -> [HandRank]:
    """
    returns all possible Poker hand ranks for input
    NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
    """
    player_hand = []
    ranks = hand_rank_calculator.calculate_all_possible_hand_ranks(player_hand)

    return ranks
