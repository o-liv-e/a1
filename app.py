def sum_list(numbers):
    """Returns the sum of all numbers in a list."""
    return sum(numbers)

def count_negatives(numbers):
    """Counts how many negative numbers are in a list."""
    return sum(1 for x in numbers if x < 0)
