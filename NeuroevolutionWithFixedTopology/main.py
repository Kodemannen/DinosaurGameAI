from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import nn_functions
import time
from selenium import webdriver
import interaction



def Evaluate_pop(population, games_per_individual):
    population_size = len(population)
    for i in range(population_size):
        current_player = population[i]
        avg_score = 0
        for game in range(games_per_individual):
            # Starting game:
            Playing = True
            agu.press("space")
            keyUp = True
            while Playing:
                screen = interaction.Screenshot_difference(region)
                output = nn_functions.Feed_forward(current_player, architecture, screen)
                
                action_index = np.argmax(output)
                #action_index = nn_functions.Sample_action(output)
                #action = output_actions[action_index]

                if action_index == 0:
                    # Do nothing
                    pass
                elif action_index == 1:
                    # Jump
                    agu.press("up")
                elif action_index == 2:
                    agu.keyDown("down")
                else:
                    agu.keyUp("down")
                
                print(action_index)
                Playing = True if driver.find_element_by_id("Playing").text == "true" else False

            score = eval(driver.find_element_by_id("Score").text)
            print("Score = " + str(score))
            avg_score += score

            time.sleep(1)
            
        avg_score = avg_score / games_per_individual
        population[i]["fitness"] = avg_score
    return population




game_url = "file:///home/kodemannen/DinosaurGameAI/t-rex-runner/index.html"
driver = webdriver.Firefox()
driver.get(game_url)
driver.set_window_position(0,0)
driver.maximize_window()
time.sleep(0.5)


# Game region:
x = 688; y = 165; w = 600; h = 150
region=(x,y,w,h)
input_size = w*h*3

agu.click(x,y)

####################
# Hyperparameters: #
####################
output_actions = ["nothing", "jump", "duck", "release_duck"]

architecture = [input_size, 64, len(output_actions)]
population_size = 2
mutation_rate = 1
games_per_individual = 2
capture_delay = 0.0    # default = 0.05


###############
# Initialize: # 
print("Initializing..")
population = nn_functions.Initialize_population(population_size, architecture)

print("Initialization complete.")
time.sleep(0.2)
print("Starting training..")

game_count=0
generation_count = 0

Training = True
while Training:

    ###################################################
    # The whole population plays a set of games each: #
    ###################################################
    population = Evaluate_pop(population, games_per_individual)
    

    #########################################
    # Tournament selection to find parents: #
    #########################################





