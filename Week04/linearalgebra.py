# -*- coding: utf-8 -*-
"""linearalgebra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QRXQsAS-4kn2l6SMYxvvTtgvapKgQh78

# Linear Algebra

"""

"""
Vector Operation
"""
# Library
import numpy as np

# Vector
a = np.array([1, 2])
b = np.array([2, 3])

# Summation
c = a + b
print(c)

c = np.add(a,b)
print(c)

# Subtraction
c = a - b
print(c)

c = np.subtract(a, b)
print(c)

# Scalar multiplication
c = 2 * a
print(c)

c = np.multiply(2, a)
print(c)

# Inner product
c = np.dot(a, b)
print(c)

c = np.inner(a, b)
print(c)

"""
Vector Norm & Inner Product
"""

import numpy as np
from scipy.spatial import distance

# Vector
a = np.array([3, 4])

# 2nd-order norm
norma = np.linalg.norm(a)
print(norma)

# Euclidean distance between two vectors
a = np.array([3, 4])
b = np.array([3, 2])
print(distance.euclidean(a, b))
print(np.linalg.norm(a-b))

# Orthogonal
a = np.array([2, 0])
b = np.array([0, 3])
print(np.inner(a, b))

"""
Matrix Operation
"""

# library
import numpy as np

# Matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 3], [4, 5]])

# Addition
print(A+B)
print(np.add(A, B))

# Subtraction
print(A-B)
print(np.subtract(A, B))

# Scalar Multiplication
print(2*A)
print(np.multiply(2, A))

# Transpose
A = np.mat([[1, 2], [3, 4]])
print(A)
print(A.T)

# Matrix Multiplcation
A = np.matrix([[0, 2, 0, 2], [1, 0, 1, 0]])
B = np.mat([[1], [2], [3], [4]])

print(A@B) # only python 3
print(np.matmul(A, B))
print(np.matmul(B, A))

"""
Various Square Matrix
"""

# Diagonal matrix
diagA = np.diag([1, 2, 4])
print(diagA)

# Identity matrix
idenA = np.identity(3)
print(idenA)

# Triangular matrix
A = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Square matrix')
print(A)
print('Upper Triangular matrix')
print(np.triu(A))
print('Lower Triangular matrix')
print(np.tril(A))

# Inverse matrix
A = np.mat([[1, 2], [1, 0]])
invA = np.linalg.inv(A)
print('Matrix A')
print(A)
print('Inverse matrix A')
print(invA)

"""
Matrix translation & Eigen Analysis
"""

# library
import numpy as np

# Matrix transform
W = np.mat([[1/np.sqrt(2), 1/np.sqrt(2)], [-1/np.sqrt(2), 1/np.sqrt(2)]])
X = np.mat([[1], [2]])
print('Translation Matrix')
print(W)
print('Matrix A')
print(X)
print('Transformed Matrix')
print(np.matmul(W, X))

# Determinant
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))

# Eigenvalue & Eigenvector
A = np.mat([[3, 1], [1, 3]])
eigVal, eigVec = np.linalg.eig(A)
print(eigVal)
print(eigVec)