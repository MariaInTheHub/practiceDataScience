import pylab
import random


def get_mean_and_std(x):
    mean = sum(x) / float(len(x))
    tot = 0.0
    for i in x:
        tot += (i - mean) ** 2
    std = (tot / len(x)) ** 0.5
    return mean, std


class Die(object):
    def __init__(self, val_list):
        """ val_list is not empty """
        if val_list:
            self.possible_vals = val_list[:]

    def roll(self):
        return random.choice(self.possible_vals)


def make_histogram(values, num_bins, label_x, label_y, title=None):
    """
      - values: a sequence of numbers
      - num_bins: a positive int
      - labels and title are strings
      - If title is provided by a caller, puts that title on the
      figure and otherwise does not title the figure

    Produces a histogram of values with num_bins bins and
      the indicated labels for the x and y axis
    """
    pylab.clf()
    pylab.hist(values, num_bins)
    pylab.xlabel(label_x)
    pylab.ylabel(label_y)
    if title:
        pylab.title(title)
    pylab.show()


# test:
# makeHistogram([1,2,3,4,5,6,6,6,7], 20, 'x', 'y')

def get_average(die, num_rolls, num_trials):
    """
      - die: a Die
      - num_rolls, num_trials: positive integers

      Calculates the expected mean value of the longest run
      of a number over num_trials runs of num_rolls rolls

      Calls makeHistogram (10 bins) to produce a histogram of the
      longest runs for all the trials. 

      Returns the mean calculated
    """

    longest_runs = []
    for t in range(num_trials):
        longest = 0
        longest_all = 0
        prev_roll = 0
        for r in range(num_rolls):
            current_roll = die.roll()
            if current_roll == prev_roll:
                longest += 1
            else:
                longest = 1
            if longest >= longest_all:
                longest_all = longest
            prev_roll = current_roll
        longest_runs.append(longest_all)

    make_histogram(longest_runs, 10, "longest run", "frequency")
    mean, std_dev = get_mean_and_std(longest_runs)
    return mean


if __name__ == "__main__":
    # tests
    print(get_average(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))

    print('test1', get_average(Die([1]), 10, 1000))
    print('test2', get_average(Die([1, 1]), 10, 1000))
    print('test3', get_average(Die([1, 2, 3, 4, 5, 6]), 50, 1000))
    print('test4', get_average(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 50, 1000))
    print('test5', get_average(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 1, 1000))
