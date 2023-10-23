from app_poker.config.high_game.hand_rank import HandRank
from app_poker.core.hand_rank_calculator.royal_flush import is_royal_flush
from app_poker.core.hand_rank_calculator.straight_flush import is_straight_flush
from app_poker.core.hand_rank_calculator.straight import is_straight
from app_poker.core.hand_rank_calculator.four_of_a_kind import is_four_of_a_kind
from app_poker.core.hand_rank_calculator.three_of_a_kind import is_three_of_a_kind
from app_poker.core.hand_rank_calculator.full_house import is_full_house

from app_poker.core.hand_rank_calculator.flush import is_flush
from app_poker.model.hand import Hand


class HandRankCalculator:
    """
    A container for all Poker Hand calculations.
    With this layout we can later inject a gateway to Poker engines like
    PokerKit from University of Toronto Computer Poker Research Group
    to calculate a rank number to use in determining a winner.
    """

    def calculate_highest_hand_rank(self, hand: Hand) -> HandRank:
        """
        Given a Poker hand.
        Calculates the highest hand rank possible.

        Computational Complexity Analysis:
            TBD

        NB: We might want to have this defined on class Hand.
            as: class Hand:
                    def calculate_highest_hand_rank(self):
                        ...
            However the highest rank possible for a Hand depends on the
            Poker rule set in use.
            It is the rule set engine's responsibility to apply the parameters
            of the match to determine the hand's rank not the hand itself.
        """
        cards = hand.cards

        if is_royal_flush(cards):
            return HandRank.ROYAL_FLUSH
        elif is_straight_flush(cards):
            return HandRank.STRAIGHT_FLUSH
        elif is_four_of_a_kind(cards):
            return HandRank.FOUR_OF_A_KIND
        elif is_full_house(cards):
            return HandRank.FULL_HOUSE
        elif is_flush(cards):
            return HandRank.FLUSH
        elif is_straight(cards):
            return HandRank.STRAIGHT
        elif is_three_of_a_kind(cards):
            return HandRank.THREE_OF_A_KIND
        # elif is_two_of_a_kind(cards):
        # elif is_one_pair(cards):
        else:
            return HandRank.HIGH_CARD

    def calculate_all_possible_hand_ranks(self, hand: Hand) -> [HandRank]:
        """
        Given a Poker hand, calculates all possible hand ranks for the cards.

        use-cases:
            1. implementing an automated player:
                The player knows there are only 7,462 distinct hand ranks.
                It can then subtract the ones possible from its cards from the
                total possible. This knowledge can be factored into the probabilities
                for what the other players have.

        NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
        """
        # TODO: a dummy default value
        ranks = [
            HandRank.STRAIGHT.name,
            HandRank.STRAIGHT_FLUSH.name,
            HandRank.HIGH_CARD.name,
        ]
        return ranks
