import numpy as np

def mandelbrot_iteration(c, max_iter = 1000, arb_limit = 1e6):
    """
    This function computes the Mandelbrot iteration for a given complex number c.
    It returns the final value of z and an array indicating the iteration at which
    the absolute value of z exceeds a specified arbitrary limit.

    Parameters:
    c : complex
        The complex number or array of numbers for which to compute the Mandelbrot iteration.
    max_iter : int, optional
        The maximum number of iterations to perform. Default is 1000.
    arb_limit : float, optional
        The arbitrary limit for the absolute value of z. Default is 1e6.
    
    Returns:
    z : complex
        The final value/s of z after the iterations.
    conv : ndarray
        An array indicating the iteration at which the absolute value of z exceeds the arbitrary limit.
    """
    z = 0 #define z

    conv = np.full((1000, 1000), max_iter) #create an array to store the iteration at which z passes the threshold

    for k in range(max_iter):
        z = z**2 + c
    
        idcs = np.where(abs(z) > arb_limit) #find where z passes the arbitrary max threshold
        z[idcs] = np.nan #set those indices to nan so we don't get a runtime error
        conv[idcs] = k #array which stores the iteration at which z passed the threshold for a given c
    
    return z, conv