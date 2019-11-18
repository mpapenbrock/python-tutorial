# Documentation: https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html

# We will have a more detailed look into plotting now
import numpy as np # We will need this for generating some distributions
import matplotlib.pyplot as plt # This is our plotting library

# Initialising the number generator with a seed
np.random.seed(1)

# Let's have something to plot
normal = np.random.normal(2,0.5,1000)
uniform = np.random.uniform(0,5,1000)
distribution = np.concatenate((normal,uniform),axis=0) # joins the two arrays
np.random.shuffle(distribution) # randomises the order of array elements

# Now we get to the plotting
plt.hist(distribution, bins=50, range=(0,5)) # Initialise a histogram with some data, number of bins, and a range to be shown
plt.xlabel('Observable') # Set a label for the x-axis
plt.ylabel('Entries') # Set a label for the y-axis
plt.title('My awesome histogram') # Give the histogram a nice title
plt.show() # Render the plot

# We can also look at all distributions in individual subplots
plt.subplot(1,3,1) # 1 row, 3 columns, 1st position
plt.hist(normal, bins=50, range=(0,5))
plt.subplot(1,3,2) # 1 row, 3 columns, 2nd position
plt.hist(uniform, bins=50, range=(0,5))
plt.subplot(1,3,3) # 1 row, 3 columns, 3rd position
plt.hist(distribution, bins=50, range=(0,5))
plt.suptitle('More histograms')
plt.show() # Render the plot

# We can also plot the distributions against each other in two dimensions
plt.hist2d(normal,uniform)
plt.xlabel('normal') # Never forget to label your plots
plt.ylabel('uniform')
plt.show()

