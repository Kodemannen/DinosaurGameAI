from selenium import webdriver
import selenium

driver = webdriver.Firefox( )
driver.get("http://wayou.github.io/t-rex-runner/")
# = driver.find_elements_by_id("distanceRan")
running_game = True
while running_game:
    try:
        tall = driver.execute_script("return distanceRan")
        print(tall)
    except selenium.common.exceptions.JavascriptException: 
        print("wait")