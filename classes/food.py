import settings
import graphics
import pygame
from random import randint


class Food:
    def __init__(self, snake_position):
        self.position = self.generate_position(snake_position)

    def generate_position(self, snake_position):
        while True:
            new_position = (
                randint(1, settings.GRID_WIDTH - 2),
                randint(2, settings.GRID_HEIGHT - 2),
            )
            if new_position not in snake_position.body:
                return new_position

    def draw(self, screen):
        screen.blit(
            graphics.frame_food,
            pygame.Rect(
                (self.position[0] * settings.GRID_SIZE),
                (self.position[1] * settings.GRID_SIZE),
                settings.GRID_SIZE,
                settings.GRID_SIZE,
            ),
        )
