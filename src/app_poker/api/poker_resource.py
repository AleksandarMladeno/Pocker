import logging
from flask import Blueprint, Response, request
from config.standard.hand_rank import HandRank
from logging import log

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
            - validate number of cards here.
            - validate cards:
                card value value
                card suit value
            - fail if the hand is empty, 422
            ...
        """
        for card in player_hand:
            if value_key not in card.keys() or suit_key not in card.keys():
                return "Incorrectly formed request", 422

        # 3. TODO: call calculator here:
        # highest_hand_rank = PokerHandCalculator.calculate_highest_hand_rank(player_hand)
        # TODO: remove default value after calculator call is implemented
        highest_hand_rank = HandRank.STRAIGHT_FLUSH.name
        log(logging.INFO, "Successfully processed user request.")
        return {"highest_rank": highest_hand_rank}, 200

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
    # ranks = PokerHandCalculator.calculate_hand_ranks(player_hand)
    ranks = [
        HandRank.STRAIGHT.name,
        HandRank.STRAIGHT_FLUSH.name,
        HandRank.HIGH_CARD.name,
    ]
    return ranks
