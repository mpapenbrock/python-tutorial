# Documentation and distributions can be found here:
# https://numpy.org/doc/1.17/reference/random/generator.html#numpy.random.Generator

# We will use the numpy package for generating random numbers
import numpy as np

# First things first!
# When working with (pseudo-)random numbers, always set a seed
# It makes the numbers reproducible
np.random.seed(1)

# Let's start with just a single number
random_number = np.random.normal() # "normal" refers to the Normal distribution
print('The random number is', random_number)

# Next, let us generate 10 random numbers at once and put them in an array
random_array = np.random.normal(size=10)
print('The random array is', random_array)

# We can also generate numbers across a desired range
# and change the distribution
random_uniform_array = np.random.uniform(low=0, high=100, size=10)
print('The random uniform distribution is', random_uniform_array)

# Let's say we want a Gaussian distribution with a specific mean and standard deviation
mean, sigma = 1, 0.2
gaussian = np.random.normal(mean, sigma, size=10)
print('The Gaussian is', gaussian)

# With only 10 numbers this is boring
# Let's generate some more and plot it
another_gaussian = np.random.normal(mean, sigma, size=1000)

# Note: Histogramming will be explained in more detail in the next part
import matplotlib.pyplot as plt
bins = 30
plt.hist(another_gaussian, bins)
plt.show()
# Did it work and did you see a Gaussian distribution?

# We can even do this in 2 dimensions
# First, we need the corresponding mean and the covariance matrix
mean2d = (1,2)
cov = [[1,0],[0,1]]
gaussian2d = np.random.multivariate_normal(mean2d, cov, 1000)

# Another plot
x, y = gaussian2d.T # get the transposed array
plt.hist2d(x,y)
plt.show()
