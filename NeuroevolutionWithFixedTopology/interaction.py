"""
Functions for interacting with a game.
"""
from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import numpy as np
import time

def Screenshot_difference(region, delay=0.0):
    """
    Takes two screenshots and returns the difference matrix
    reshaped into a row vector.
    
    Arguments
    ----------
    region : tuple/list 
        (x,y,width,height) 
    delay : scalar
        Time delay between the two screen captures.

    Returns
    -------
    diff : NumPy column vector shape=(input_size, 1)
        Numbers between 0 and 1
    """
    input_size = region[2]*region[3]*3
    screen1 = np.array(agu.screenshot(region=region))
    time.sleep(delay)
    screen2 = np.array(agu.screenshot(region=region))
    diff = (screen2-screen1).reshape(input_size) / 255  - 1
    return diff

