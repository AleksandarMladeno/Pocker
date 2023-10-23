from collections import defaultdict


def count_occurrences(values: []):
    """
    Generic function to count the number
    of occurrences of a value in a list.
    """
    occurrences_counts = defaultdict(lambda: 0)
    for card_rank in values:
        occurrences_counts[card_rank] += 1
    return occurrences_counts
