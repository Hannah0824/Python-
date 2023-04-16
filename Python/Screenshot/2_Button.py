from PIL import Image
import pyautogui as pag 
import time 
import keyboard 
import pygame 

pygame.init()
screen = pygame.display.set_mode((10,10))
pygame.display.set_caption("Screenshot")

filepath = 'C:\\Users\\user\\Documents\\Python\\Screenshot\\images'

def screenshot():
    curr_time= time.strftime("_%Y%m%d_%H%M%S") 
    pag.screenshot(f"{filepath}/image{curr_time}.png")

running=True 
while running: 

    for event in pygame.event.get(): 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LCTRL : 
                screenshot()
            elif event.key == pygame.K_LSHIFT: 
                running = False 

pygame.quit()
