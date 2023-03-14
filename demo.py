import os
import pygame
import time

# configuration
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((480, 320), pygame.FULLSCREEN)
pygame.mouse.set_visible(0)

# set up the colors
b = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
c = (0, 255, 255)
p = (255, 0, 255)

# update screen with fill color
lcd.fill(c)
pygame.display.update()
time.sleep(1)

lcd.fill(p)
pygame.display.update()
time.sleep(1)

lcd.fill(w)
pygame.display.update()
time.sleep(1)
