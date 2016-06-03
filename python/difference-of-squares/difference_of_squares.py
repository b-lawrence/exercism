"""
Difference between the sum of
the squares and the square of
the sums of the first N natural numbers.
"""


def square_of_sum(n):
    """Square of sum"""
    return sum(xrange(1, n + 1)) ** 2


def sum_of_squares(n):
    """Sum of squares"""
    return sum([digit**2 for digit in xrange(1, n + 1)])


def difference(n):
    """Difference"""
    return abs(sum_of_squares(n) - square_of_sum(n))
