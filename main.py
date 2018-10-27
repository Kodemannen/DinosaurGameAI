from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import functions

from selenium import webdriver
game_url = "file:///home/kodemannen/DinosaurGameAI/t-rex-runner/index.html"
driver = webdriver.Firefox()
driver.get(game_url)

# game window coordinates (x,y,width,height):
x = 688
y = 165
width = 600
height = 150
region=(x,y,width,height)


#################################
# Initializing neural networks: #
#################################
output_actions = ["nothing", "up", "down"]
input_size = width*height




#screen = agu.screenshot(region=(x,y,w,h))

#plt.imshow(screen)
#plt.show()

# while True:
#     get_score = driver.find_element_by_id("Score")
#     get_playing = driver.find_element_by_id("Playing")
    
    
    
    # try:
    #     print(float(element.text))
    # except ValueError:
    #     None