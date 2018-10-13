from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import functions
import time
from selenium import webdriver


def Screenshot_difference(region, input_size, delay=0.05):
    ####################################################
    # Takes two screenshots and returns the difference #
    ####################################################   
    screen1 = np.array(agu.screenshot(region=region))
    time.sleep(delay)
    screen2 = np.array(agu.screenshot(region=region))
    diff = (screen2-screen1).reshape(input_size, 1) / 255
    return diff
    
def Initialize_genome(architecture):
    L = len(architecture)   # total number of layers
    genome = {}
    for l in range(L-1):
        W = np.random.randn(architecture[l+1],architecture[l])*np.sqrt(2/architecture[l])
        b = np.zeros(shape=(architecture[l+1],1))
        genome["W%s"%(l+1)] = W
        genome["b%s"%(l+1)] = b
    return genome

def Initialize_population(population_size, architecture):
    population = []
    for i in range(population_size):
        genome = Initialize_genome(architecture)
        population.append(genome)
    return population

def Mutate():
    return None

def Crossover():
    return None

def Tournament_selection():
    return None