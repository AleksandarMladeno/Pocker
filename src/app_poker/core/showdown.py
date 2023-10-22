from app_poker.model.hand import Hand


def decide_winner(hands: [Hand]) -> Hand:
    """
    objective: Determines who wins the pot.
    return value: Returns winning hand.

    This would apply different winning rules based on the Poker style(i.e. rule-set at play)
    example:
        for High games:
            find and return hand with the highest hand rank.
        for Low games:
            find and return hand with the lowest hand rank.
        for High-Low split games:
            based on the High-Low hand and card ranks:
                find hand with the lowest hand rank.
                            and
                find hand with the highest hand rank.

            return both hands

     NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
    """
    pass
