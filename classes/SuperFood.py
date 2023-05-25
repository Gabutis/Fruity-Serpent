from random import randint
import settings
import graphics
import pygame


class SuperFood:
    def __init__(self):
        self.position = None
        self.timer = 0
        self.start_time = pygame.time.get_ticks()
        self.spawn_interval = randint(1, 3)
        self.food_spawns = 0

    def update(self, snake_position):
        if self.food_spawns >= self.spawn_interval:
            self.food_spawns = 0
            self.spawn_interval = randint(1, 3)
            self.generate_position(snake_position)

    def generate_position(self, snake_position):
        while True:
            new_position = (
                randint(1, settings.GRID_WIDTH - 2),
                randint(2, settings.GRID_HEIGHT - 2),
            )
            if new_position not in snake_position.body:
                self.position = new_position
                return self.position

    def draw(self, screen):
        if self.position is not None:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 500
            if elapsed_time >= 1:
                self.start_time = pygame.time.get_ticks()
                self.timer += 1
                if self.timer > 7:
                    self.timer = 0
                    self.position = None

        if self.position is not None:
            screen.blit(
                getattr(graphics, f"frame_superfood{self.timer}"),
                pygame.Rect(
                    self.position[0] * settings.GRID_SIZE,
                    self.position[1] * settings.GRID_SIZE,
                    settings.GRID_SIZE,
                    settings.GRID_SIZE,
                ),
            )
