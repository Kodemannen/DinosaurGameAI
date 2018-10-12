from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import pyautogui as agu
import time
import matplotlib.pyplot as plt
import numpy as np
import functions

from selenium import webdriver
game_url = "file:///home/kodemannen/t-rex-runner/index.html"
driver = webdriver.Firefox()
driver.get(game_url)

game window coordinates (x,y,width,height):
x = 688
y = 165
w = 600
h = 120
region=(x,y,w,h)

screen = agu.screenshot(region=(x,y,w,h))



# while True:
#     get_score = driver.find_element_by_id("Score")
#     get_playing = driver.find_element_by_id("Playing")
    
    
    
    # try:
    #     print(float(element.text))
    # except ValueError:
    #     None