"""
Functions for creating and manipulating dense neural networks
through evolutionary means.
"""

from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import time
from selenium import webdriver


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
    nn["fitness"] = 0
    L = len(architecture)
    for l in range(1, L):
        W_l = np.random.randn(architecture[l], architecture[l-1]) * np.sqrt(architecture[l-1])
        b_l = np.zeros(shape=(architecture[l]))
        nn["W_%s" % l] = W_l
        nn["b_%s" % l] = b_l
    return(nn)

def Initialize_population(population_size, architecture):
    population = []
    for i in range(population_size):
        genome = Initialize_nn(architecture)
        population.append(genome)
    return population


def Feed_forward(individual, architecture, screen):
    L = len(architecture)
    h = screen
    for l in range(1,L):
        W_l = individual["W_%s" % l]
        b_l = individual["b_%s" % l]
        h = ReLu(np.dot(W_l, h) + b_l)
    output = Softmax(h)
    return output

def Sample_action(output):
    chosen_index = np.random.choice(output.shape[0],p=output)
    return chosen_index

def ReLu(vec):
    return vec*(vec > 0)

def Softmax(vec):
    exped = np.exp(vec-np.max(vec))
    softmaxed = exped / np.sum(exped)
    return softmaxed

def Mutate():
    return None

def Crossover():
    return None

def Tournament_selection():
    return None