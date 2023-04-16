from PIL import Image
import pyautogui as pag 
import time 

time.sleep(3)

filepath = 'C:\\Users\\user\\Documents\\Python\\Screenshot\\images'

for i in range(1,6):
    curr_time= time.strftime("_%Y%m%d_%H%M%S") #formatting 
    pag.screenshot(f"{filepath}/image{curr_time}.png")
    time.sleep(2)