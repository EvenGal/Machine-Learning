import numpy

def mean_of_set(set):
    """
    Returns the mean of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated mean of set
    """
    x = numpy.mean(set)

    return x


def median_of_set(set):
    """
    Returns the median of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated median of set
    """
    x = numpy.median(set)

    return x


def mode_of_set(set):
    """
    Returns the mode of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated mode of set
    """
    x = numpy.mode(set)

    return x


def standard_deviation_of_set(set):
    """
    Returns the standard deviaton of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated standard deviation of set
    """
    x = numpy.mode(set)

    return x


def variance_of_set(set):
    """
    Returns the variance of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated variance of set
    """
    x = numpy.var(set)

    return x


def percentile_of_set(set, percentile):
    """
    Returns the percentile of the set.

    Args:
        set: a set of numbers
    Returns:
        x: calculated percentile of set
    """
    x = numpy.percentile(set, percentile)

    return x


def uniform_set(set, value, amount):
    """
    Returns a random set of numbers between values * amount times of the set.

    Args:
        set: a set of numbers
        value: the values we are creating numbers between
        amount: how many of these values we are creating
    Returns:
        x: a set with numbers between values * amount times
    """
    x = numpy.random.uniform(set, value, amount)

    return x
