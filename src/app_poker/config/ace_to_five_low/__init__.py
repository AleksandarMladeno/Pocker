"""
    The hand_rank module for ace_to_five_low would exclude straights, flushes and straight flushes.
    Hence the config are separated into different modules.
    To support more Poker variants the PokerHandCalculator module would have
    to be told which Poker game variant is it expected to run calculations
    against and use the appropriate config.

    NB: Not necessary for current objective.
        Added it to paint a full picture, to design to a system that would
        be extensible for modelling and solving Poker problems.
"""
