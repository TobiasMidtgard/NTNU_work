import pygame
import random


class Ball():
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)

    def check_collision(self, width, height):
        crashed = False

        if self.x >= width - self.radius or self.x <= 0 + self.radius:
            self.dx *= -1
            crashed = True
        if self.y >= height - self.radius or self.y <= 0 + self.radius:
            self.dy *= -1
            crashed = True
        return crashed

    def play_collision_sound(self, sound):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pygame.draw.circle(self.surface, self.color,
                           (self.x, self.y), self.radius)
