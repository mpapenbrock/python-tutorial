# Documentation: https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html

import numpy as np

# We define a simple matrix
a = np.matrix([[1, 2], [3, 4]])
print('The matrix a is')
print(a)

# Let's look into some operations on the matrix itself
# For a full list follow the link above
print('The diagonal of a is')
print(a.diagonal())

print('The inverse of a is')
print(a.getI())

print('The transpose of a is')
print(a.getT())

# Multiplication is not an issue either
print('Multiplying a with 3 gives')
print(3 * a)

# We can also muliply with another matrix
b = np.matrix([[5, 6], [7, 8]])
print('Multiplying a with b yields')
print(np.matmul(a, b))

# Or with a vector
c = np.array([1, 2])
print('The dot product of a and c is')
print(np.dot(a, c))