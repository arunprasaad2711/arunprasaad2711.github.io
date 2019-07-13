# Pygame
It is a simple gaming library framework for Python.

## Installation
Use anyone of the following:
* Conda
* pip
* wheel packages

## Mandatory requirement
```Python
import pygame

# This initializes all the functions inside the module
# this init function returns a tuple if the initialization is successful
pygame.init()

# This is a surface
# creating a display surface object with width:height = 8:6
gameDisplay = pygame.display.set_mode((800, 600))

# this updates the entire surface/canvas
pygame.display.flip()
# this updates the specific region of the surface
pygame.display.update()
# use either one of them

# closes the functions
pygame.quit()
# quit the screen
quit()
```

## Title
```Python
pygame.display.set_caption("title")
```
