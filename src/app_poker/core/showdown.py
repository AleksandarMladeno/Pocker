from model.hand import Hand


def decide_winner(hands: [Hand]) -> Hand:
    """
    NB: purely for gaining a big picture to design for, we will not be implementing this for this task.

    determines who wins the pot.
    returns winning hand

    This would apply different winning rules based on the Poker style(i.e. ruleset at play)
    example:
        for High games:
            find hand with the lowest numbered rank
        for Low games:
            find hand with the highest numbered rank
        for High-Low split games:
            find hand with the lowest numbered rank
                            and
            find hand with the highest numbered rank

            based on the High-Low rank and card ranks
    """
    pass
