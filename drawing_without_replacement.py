import random


def drawing_without_replacement(num_trials):
    """
    Runs numTrials trials of a Monte Carlo simulation of drawing 
    3 balls out of a bucket containing 4 red and 4 green balls. 
    Balls are not replaced once drawn. 
    Returns a float - the fraction of times 3 balls of the same color 
    were drawn in the first 3 draws. 
    """
    #    Solution without use of functions or methods from pylab, numpy, or matplotlib.

    one_color = 0
    for i in range(num_trials):
        bucket = [0, 0, 0, 0, 1, 1, 1, 1]
        if sum(random.sample(bucket, 3)) in (0, 3):
            one_color += 1
    return float(one_color / num_trials)


if __name__ == "__main__":
    print(drawing_without_replacement(1000000))
    # output: 0.142776 = OK = 1/7 = 0,142857...
