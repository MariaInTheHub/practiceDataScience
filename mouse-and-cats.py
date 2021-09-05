import random
import pylab

MAX_MICE_POP = 1000
CURRENT_MICE_POP = 500
CURRENT_CAT_POP = 30


def mouse_reprod():
    """ 
    mouse_reprod is called once at the beginning of each time step.

    It makes use of the global variables: CURRENT_MICE_POP and MAX_MICE_POP.

    The global variable CURRENT_MICE_POP is modified by this procedure.

    For each mouse, based on the probabilities in the problem set write-up, 
      a new mouse may be born.
    Nothing is returned.
    ###
    never fewer than 10 mice; the maximum population of mice is 1000
    each mouse during each time step, a new mouse will be born with a probability of 
p_mouse_reproduction = 1.0 - (CURRENT_MICE_POP/MAX_MICE_POP)
    """
    global CURRENT_MICE_POP

    for mouse in range(CURRENT_MICE_POP):
        if MAX_MICE_POP <= 1000:
            if random.random() <= 1.0 - (CURRENT_MICE_POP / MAX_MICE_POP):
                CURRENT_MICE_POP += 1


def cat_reprod():
    """ 
    cat_reprod is called once at the end of each time step.

    It makes use of the global variables: CURRENT_CAT_POP and CURRENT_MICE_POP,
        and both may be modified by this procedure.

    Each cat, based on the probabilities in the problem statement, may eat 
      one mouse (but only if there are more than 10 mice).

    If it eats a mouse, then with a 1/3 prob it gives birth to a new cat.

    If it does not eat a mouse, then with a 1/10 prob it dies.

    Nothing is returned.
    ##
    never fewer than 10 Cats
    p cat eats mouse = (CURRENT_MICE_POP/MAX_MICE_POP)
    if a cat succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.
If a cat fails in hunting then it has a 10 percent chance of dying in the current time-step.
    """
    global CURRENT_MICE_POP
    global CURRENT_CAT_POP

    for cat in range(CURRENT_CAT_POP):
        if CURRENT_MICE_POP > 10 and random.random() <= CURRENT_MICE_POP / MAX_MICE_POP:  # hunting
            CURRENT_MICE_POP -= 1
            if random.random() <= 1 / 3:  # reproducing
                CURRENT_CAT_POP += 1
        elif CURRENT_CAT_POP > 10 and random.random() <= 0.9:  # 0.1: # dying
            CURRENT_CAT_POP -= 1


def run_simulation(num_steps):
    """
    Runs the simulation for `num_steps` time steps.

    Returns a tuple of two lists: (mouse_populations, cat_populations)
      where mouse_populations is a record of the mouse population at the 
      END of each time step, and cat_populations is a record of the cat population
      at the END of each time step.

    Both lists should be `num_steps` items long.
    """

    mouse_populations = []
    cat_populations = []
    for step in range(num_steps):
        mouse_reprod()
        cat_reprod()
        mouse_populations.append(CURRENT_MICE_POP)
        cat_populations.append(CURRENT_CAT_POP)

    pylab.clf()
    pylab.plot([step for step in range(num_steps)], mouse_populations, label='Mice population')
    pylab.plot([step for step in range(num_steps)], cat_populations, label='Cat population')
    pylab.legend(loc='best')
    pylab.title('Cat and Mice Population')
    pylab.xlabel('Step')
    pylab.ylabel('Population')

    coeff = pylab.polyfit(range(len(mouse_populations)), mouse_populations, 2)

    pylab.plot(pylab.polyval(coeff, range(len(mouse_populations))))

    return list(zip(mouse_populations, cat_populations))


if __name__=="__main__":
    run_simulation(200)

# Test with Global Variables
# MAX_MICE_POP = 1000
# CURRENT_MICE_POP = 50
# CURRENT_CAT_POP = 300
