from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import functions
import time
from selenium import webdriver

game_url = "file:///home/kodemannen/DinosaurGameAI/t-rex-runner/index.html"
driver = webdriver.Firefox()
driver.get(game_url)

# Game region:
x = 688; y = 165; w = 600; h = 120
region=(x,y,w,h)
input_size = w*h*3

####################
# Hyperparameters: #
####################
output_actions = ["nothing", "up", "down"]
architecture = [input_size, 64, len(output_actions)]
population_size = 20
mutation_rate = 1
games_per_individual = 5

# Initialize population: 
population = functions.Initialize_population(population_size, architecture)


# while True:
# #     get_score = driver.find_element_by_id("Score")
# #     get_playing = driver.find_element_by_id("Playing")
#     diff = functions.screenshot_difference(region=region, input_size=input_size, delay=0.07)    
#     print(np.linalg.norm(diff))
    
#     # try:
#     #     print(float(element.text))
#     # except ValueError:
#     #     None