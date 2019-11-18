# We will have a more detailed look into plotting now
import numpy as np # We will need this for generating some distributions
import matplotlib.pyplot as plt # This is our plotting library
from scipy.optimize import curve_fit # We will use this for fitting

# Initialising the number generator with a seed
np.random.seed(1)

# Let's have something to plot
normal = np.random.normal(2,0.5,1000)
uniform = np.random.uniform(0,5,1000)
distribution = np.concatenate((normal,uniform),axis=0) # joins the two arrays
np.random.shuffle(distribution) # randomises the order of array elements

# Define a fit function
def fitfunc(x,*parameters):
  height, mean, sigma, offset = parameters # These will later be filled with the start_params
  return height*np.exp(-(x-mean)**2/(2*sigma**2)) + offset # The actual function, gaus + constant

# Transform our data into a histogram
# Since we want to work with it and not yet plot it, we use numpy
hist, bin_edges = np.histogram(distribution,density=True)
bin_centres = (bin_edges[:-1] + bin_edges[1:])/2

# Define some starting parameters ("educated guesses")
start_params = [50,1,1,10]

coeff, var_matrix = curve_fit(fitfunc,bin_centres,hist,p0=start_params)

# Get the fitted curve
hist_fit = fitfunc(bin_centres, *coeff)

# Print out the fit values
print('Fitted mean = ', coeff[1])
print('Fitted sigma = ', coeff[2])

# While we're at it, let's plot the results
plt.scatter(bin_centres, hist, label='Distribution')
plt.plot(bin_centres, hist_fit, color='red', label='Fit')
plt.show()