import pygame
import sys
from assets.Ball import Ball


def setup():
    # initialize pygame
    pygame.init()
    pygame.display.set_caption("Bouncing Ball")

    width = 800
    height = 800

    radius = 15
    x = width/2 - radius
    y = height/2 - radius

    sound = "./sound/sfx-boing3.mp3"

    # game screen
    screen = pygame.display.set_mode((width, height))

    # make ball
    ball = Ball(screen, "#ff0000", x, y, radius)

    # fps cap
    clock = pygame.time.Clock()

    return screen, clock, ball, width, height, sound


def update(ball, width, height, sound):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # exit pygame
            sys.exit()  # end program
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    collision = ball.check_collision(width, height)
    if collision:
        ball.play_collision_sound(sound)
    ball.update()


def draw(screen, ball):
    screen.fill("#000000")
    ball.draw()


def animation(screen, clock, ball, width, height, sound):
    update(ball, width, height, sound)
    draw(screen, ball)
    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)
