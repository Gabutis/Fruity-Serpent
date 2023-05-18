from random import randint
import pygame
import settings
import graphics
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def grow(self):
        taill = self.body[-1]
        self.body.append(taill)

    def draw(self, screen):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, segment in enumerate(self.body):
            block_rect = pygame.Rect(segment[0] * settings.GRID_SIZE, segment[1] * settings.GRID_SIZE, settings.GRID_SIZE, settings.GRID_SIZE)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - segment
                next_block = self.body[index - 1] - segment
                if previous_block.x == next_block.x:
                    screen.blit(graphics.frame_bv, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(graphics.frame_bh, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(graphics.frame_bbl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(graphics.frame_btl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(graphics.frame_bbr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(graphics.frame_btr, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = graphics.frame_hl
        elif head_relation == Vector2(-1, 0): self.head = graphics.frame_hr
        elif head_relation == Vector2(0, 1): self.head = graphics.frame_ht
        elif head_relation == Vector2(0, -1): self.head = graphics.frame_hb

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = graphics.frame_tl
        elif tail_relation == Vector2(-1, 0): self.tail = graphics.frame_tr
        elif tail_relation == Vector2(0, 1): self.tail = graphics.frame_tt
        elif tail_relation == Vector2(0, -1): self.tail = graphics.frame_tb

    def check_collision(self):
        if self.body[0][0] < 1 or \
                self.body[0][0] >= settings.GRID_WIDTH - 1 or \
                self.body[0][1] < 2 or \
                self.body[0][1] >= settings.GRID_HEIGHT - 1:
            return True
        for segment in self.body[1:]:
            if segment == self.body[0]:
                return True
        return False


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return randint(1, settings.GRID_WIDTH - 2), randint(2, settings.GRID_HEIGHT - 2)

    def draw(self, screen):
        screen.blit(graphics.frame_food, pygame.Rect((self.position[0] * settings.GRID_SIZE), (self.position[1] * settings.GRID_SIZE), settings.GRID_SIZE, settings.GRID_SIZE))
