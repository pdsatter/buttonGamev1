import pygame, sys, math
import os
import time
import random

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 750, 750
background = 'black'
bg = background

game = 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def buttongame_timed():
    # pygame.init()
    return None


def buttongame_toNumber(num):
    # Call function with number to reach
    repeat = True
    maxScore = num
    while repeat:
        score = 0

        while score < maxScore:
            score += 1
            # IF USER CLICK ON OBJECT, score++
            # Despawn object
            # Create new object
        # Create Menu labeled 'repeat, try again' : 'Yes', 'No'

    return None


def main():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Button Clicker Game")
    WIN.fill(bg)
    pygame.display.update()

    run = True
    FPS = 60
    clock = pygame.time.Clock()
    timer = 0

    score = 0

    def drawCircle():
        drawCircle.posW = random.random() * WIDTH  # drawCircle.variable allows universal call to variable
        drawCircle.posH = random.random() * HEIGHT
        drawCircle.rad = 20
        pygame.draw.circle(WIN, RED, [drawCircle.posW, drawCircle.posH], drawCircle.rad)
        pygame.display.flip()

    def drawClock():
        # rect = (WIDTH/2, 20, 30,15)
        clockWIDTH = 70
        clockHEIGHT = 50
        rect = pygame.draw.rect(WIN, WHITE, ((WIDTH - clockWIDTH - 10), 2, clockWIDTH, clockHEIGHT), 0)

    def redraw_window():  # updates window 'WIN'
        WIN.fill(bg)
        drawCircle()
        drawClock()
        pygame.display.update()

    redraw_window()  # sets initial dot
    drawClock()
    while run:
        clock.tick(FPS)
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]  # array [x,y]

        for event in pygame.event.get():  # QUITS if x is clicked
            if event.type == pygame.QUIT:  # shutdown
                run = False
            elif pygame.mouse.get_pressed()[0]:  # if click == True
                if (abs(x - drawCircle.posW) < drawCircle.rad) & (abs(y - drawCircle.posH) < drawCircle.rad):
                    # if clicks on circle
                    redraw_window()
                    score += 1

        if game == 1 & score == 20:  # Game 1 is a game where you reach 20 and it gives time
            timer = (pygame.time.get_ticks()) / 1000  # FIXME
            run = False  # shutdown when game ends


if __name__ == '__main__':
    main()
    # Create play again loop to keep calling main
