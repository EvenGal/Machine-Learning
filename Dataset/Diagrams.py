from Dataset import eksempel_sett
import matplotlib.pyplot as plt
from scipy import stats

def histogram_of_set(set, amount_of_bars=None):
    """
    Returns a histogram plot of set

    Args:
        set: a set of numbers
    Returns:
        plt: a histogram plot
    """
    if amount_of_bars:
        plt.hist(set, amount_of_bars)
        plt.show()
    else:
        plt.hist(set)
        plt.show()


def normal_distribution_of_set(mean, sd, amount):
    """
    Returns a normal distribution plot

    Args:
        mean: the mean of the set
        sd: the standard deviaton of set
        amount: the amount of values in set
    Returns:
        plt: a normal distribution of set
    """
    x = numpy.random.normal(mean, sd, amount)
    # 100 bars
    plt.hist(x, 100)
    plt.show()


def scatter_plot_of_set(set1, set2):
    """
    Returns a scatter plot of the two sets

    Args:
        set1: the first dataset
        set2: the second dataset
    Returns:
        plt: a scatter plot of sets
    """
    plt.scatter(set1, set2)
    plt.show()


def linear_regression_of_set(set1, set2):
    """
    Returns a linear regression plot of the two sets

    Args:
        set1: the first dataset
        set2: the second dataset
    Returns:
        plt: a scatter plot of sets
    """
    slope, intercept, r, p, std_err = stats.linregress(set1, set2)
    def myfunc(set1):
        return slope * set1 + intercept
    mymodel = list(map(myfunc, set1))
    plt.scatter(set1, set2)
    plt.plot(set1, mymodel)
    plt.show()


def relationship_of_set(set1, set2):
    """
    Returns the relationship of the two sets

    Args:
        set1: the first dataset
        set2: the second dataset
    Returns:
        r: the relationship of the two sets
    """
    slope, intercept, r, p, std_err = stats.linregress(set1, set2)
    print(r)




