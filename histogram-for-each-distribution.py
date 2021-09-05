import numpy as np
import matplotlib.pyplot as plt
"""
Given:
two normal distributions, first (F) and second (S). 
The standard deviation of F is 3 and the standard deviation of S is 5. 
Do:
For each distribution, 1,000 observations are drawn and plotted in a histogram 
with 10 bins, creating one histogram for each distribution
"""
# numpy.random.normal(mean, Standard deviation, size=None)
F = np.random.normal(0, 3, 1000)
S = np.random.normal(0, 5, 1000)
plt.clf()
plt.hist(S, bins=10)
plt.hist(F, bins=10)

plt.show()
