#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def check_divergence(c, max_iter, n_points, x_max, x_min, y_max, y_min):

    """
    
    This function check for divergence of a complex number.

    Parameters:
    
    c : complex 
        The complex number for which divergence is being checked.
    max_iter : int
        The maximum number of iterations to check for divergence.
    n_points : int
        The number of points along each dimension (real and imaginary) to generate the grid.
    x_max : float
        The maximum value of the real part (x-axis) of the complex numbers.
    x_min : float
        The minimum value of the real part (x-axis) of the complex numbers.
    y_max : float
        The maximum value of the imaginary part (y-axis) of the complex numbers.
    y_min : float
        The minimum value of the imaginary part (y-axis) of the complex numbers.

    Returns:
    
    int: The number of iterations required for divergence to be detected,
    
    or max_iter if divergence is not detected within the maximum number of iterations.
        
    """

    z0 = 0

    for i in range(max_iter):
        z = z0**2 + c
        if abs(z) > np.sqrt(x_max**2 + y_max**2):
            return i
        z0 = z  # Update z0 for the next iteration
    return max_iter


# In[3]:


# Define the parameters
n_points = 1
max_iter = 1
x_max=1
x_min=-1 
y_max=1 
y_min=-1


# In[4]:


def complex_set(n_points, max_iter, x_max, x_min, y_max, y_min):
    
    """
    
    This function creates a grid of complex numbers over a specified range in the
    complex plane and checks each point for divergence within a given number of 
    iterations. It returns an array indicating the number of iterations taken for 
    divergence and a boolean array indicating whether each point has diverged.

    Parameters:
    
    n_points : int
        The number of points along each dimension (real and imaginary) to generate the grid.
    max_iter : int
        The maximum number of iterations to check for divergence.
    x_max : float
        The maximum value of the real part (x-axis) of the complex numbers.
    x_min : float
        The minimum value of the real part (x-axis) of the complex numbers.
    y_max : float
        The maximum value of the imaginary part (y-axis) of the complex numbers.
    y_min : float
        The minimum value of the imaginary part (y-axis) of the complex numbers.

    Returns:
    
    divergence_iterations : numpy.ndarray
        A 2D array of shape (n_points, n_points) where each entry represents the number 
        of iterations taken for the corresponding complex number to diverge.
        
    diverged : numpy.ndarray
        A 2D boolean array of shape (n_points, n_points) where each entry indicates 
        whether the corresponding complex number has diverged (True) or not (False).
    
    """

    # Generate the grid of complex numbers
    x = np.linspace(x_min, x_max, n_points)
    y = np.linspace(y_min, y_max, n_points)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialize arrays to store the results
    divergence_iterations = np.zeros_like(Z, dtype=int)
    diverged = np.zeros_like(Z, dtype=bool)

    # Check for divergence for each point
    for i in range(n_points):
        for j in range(n_points):
            c = Z[i, j]
            divergence_iterations[i, j] = check_divergence(c, max_iter, n_points, x_max, x_min, y_max, y_min)
            if divergence_iterations[i, j] == max_iter:
                diverged[i, j] = True

    return divergence_iterations, diverged

