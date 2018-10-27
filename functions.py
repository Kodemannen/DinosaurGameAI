from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import numpy as np

def Initialize_nn(architecture):
    """
    Initializing a randomized dense neural network (nn) with a given architecture.

    Parameters
    ----------
    architecture : list/array
        Contains the number of nodes for each layer in the nn that is to be created.

    Returns
    -------
    nn : dictionary
        contains the weight matrices and bias vectors of the nn
    """
    nn = {}
    L = len(architecture)
    for l in range(1, L):
        W_l = np.random.randn(architecture[l], architecture[l-1]) * np.sqrt(architecture[l-1])
        b_l = np.zeros(shape=(architecture[l],1))
        nn["W_%s" % l] = W_l
        nn["b_%s" % l] = b_l
    return(nn)

