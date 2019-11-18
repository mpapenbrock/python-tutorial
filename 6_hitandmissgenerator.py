import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234) # seed for the RNG

N = 2000 # number of events to be generated
alpha = 0.2 # ratio between G_E and G_M
bins = 100 # number of bins for the histogram

def hit_miss_generator(N, alpha):
  costheta = np.random.uniform(-1, 1, size=N) # generate uniform costheta distribution
  rands = np.random.uniform(0, 1, size=N) # generate numbers for hit or miss criterion
  dsdcostheta = 1 + alpha * costheta**2 # angular distribution factor
  upper_limit = 1 + abs(alpha) # determine the upper limit
  mask = rands < dsdcostheta/upper_limit # hit or miss criterion
  return costheta[mask]

samples = []
while len(samples) < N: # repeat until we have N entries
  costheta = hit_miss_generator(N,alpha) # run the generator
  samples.extend(costheta) # append the new results

samples = samples[:N] # cut off any excess



# Let's look at the result
plt.hist(samples, bins)
plt.xlabel('costheta')
plt.ylabel('entries')
plt.show()
