"""
Functions related to the graphics of the game

This module contains functions that are used to display the game to the user.

Functions:
    - initwindow: Initializes the game window and returns the screen, clock, and initial position.
    - draw_grid: Draws a grid on the given screen.
    - draw_square: Draws a square on the given screen at the specified position.
    - handlemovement: Handles the movement of the player based on the key pressed.

Typical usage example:
    screen, clock, position = initwindow()
    while running:
        draw_grid(screen)
        draw_square(screen, position)
        pygame.display.flip()
"""
import pygame
import random
import sys

import gamefunctions

# Define constants
gridSize = 10
cellSize = 32
windowSize = gridSize * cellSize

class WanderingMonster:
    def __init__(self):
        self.position = [random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)]
        self.data = gamefunctions.random_monster()

    def move(self):
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'right' and self.position[0] < gridSize - 1:
            self.position[0] += 1
        elif direction == 'up' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'down' and self.position[1] < gridSize - 1:
            self.position[1] += 1

def init_window():
    """
    Initializes the game window and returns the screen, clock, and initial position.

    Arguments:
        None

    Returns:
        screen (pygame.Surface): The game screen.
        clock (pygame.time.Clock): The game clock.
        position (list): The initial position of the player.
    """
    pygame.init()

    screen = pygame.display.set_mode((windowSize, windowSize))
    pygame.display.set_caption('Adventure Game')

    clock = pygame.time.Clock()

    position = [0, 0]

    return screen, clock, position

def draw_grid(screen):
    """
    Draws a grid on the given screen.

    Arguments:
        screen (pygame.Surface): The game screen where the grid will be drawn.

    Returns:
        None
    """
    for x in range(0, windowSize, cellSize):
        pygame.draw.line(screen, (0,0,0), (x, 0), (x, windowSize))
    for y in range(0, windowSize, cellSize):
        pygame.draw.line(screen, (0,0,0), (0, y), (windowSize, y))

def draw_square(screen, position, type):
    """
    Draws a square on the given screen at the specified position.

    Arguments:
        screen (pygame.Surface): The game screen where the square will be drawn.
        position (list): The position [x, y] where the square will be drawn.
        type (str): The type of square to be drawn ('player' or 'monster'). This is used to determine what asset is used.

    Returns:
        None
    """
    try:
        image = None
        if type == 'player':
            image = pygame.image.load('assets/player.png')
        elif type == 'monster':
            image = pygame.image.load('assets/monster.png')
        pygame.transform.scale(image, (cellSize, cellSize))
        screen.blit(image, (position[0] * cellSize, position[1] * cellSize))
    except FileNotFoundError:
        if type == 'player':
            color = (0,0,0)
        elif type == 'monster':
            color = (255,0,0)
        rect = pygame.Rect(position[0] * cellSize, position[1] * cellSize, cellSize, cellSize)
        pygame.draw.rect(screen, color, rect)
    except Exception as e:
        print('You find yourself in a weird place. Here\'s the error we got', e)

def handle_movement(key, position):
    """
    Handles the movement of the player based on the key pressed.

    Arguments:
        key (int): The key pressed by the user.
        position (list): The current position of the player [x, y].

    Returns:
        None
    """
    if key == pygame.K_LEFT:
        if position[0] > 0:
            position[0] -= 1
    elif key == pygame.K_RIGHT:
        if position[0] < gridSize - 1:
            position[0] += 1
    elif key == pygame.K_UP:
        if position[1] > 0:
            position[1] -= 1
    elif key == pygame.K_DOWN:
        if position[1] < gridSize - 1:
            position[1] += 1
running = True
def main(monsters):
    """
    Main function to run the game.

    Parameters:
        monsters: list of WanderingMonster objects to be displayed on the screen

    Returns:
        A tuple containing a flag ('f' or 'm' for example) and the monster object if it is needed.
    """
    screen, clock, position = init_window()

    move_counter = 0
    global running
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_m:
                    running = False
                    return 'm', None
                elif event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    handle_movement(event.key, position)
                    move_counter += 1
                    if move_counter % 2 == 0:
                        for monster in monsters:
                            monster.move()
        for monster in monsters:
            if position == monster.position:
                return 'f', monster

        screen.fill((255,255,255))
        draw_grid(screen)
        draw_square(screen, position, 'player')
        for monster in monsters:
            draw_square(screen, monster.position, 'monster')
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()