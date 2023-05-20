from random import randint
import pygame
import settings
import graphics
from pygame.math import Vector2


from random import randint
import pygame
import settings
import graphics
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)
        self.score = 0

    def move(self, food_position, auto_move=False):
        head = self.body[0]

        if auto_move:
            next_direction = self.move_towards_food(Vector2(food_position))
            # Check if moving in the next direction would result in a collision with the body
            if self.is_valid_direction(next_direction):
                self.direction = next_direction
            else:
                # Find the next valid direction to move
                next_direction = self.find_next_valid_direction()
                self.direction = next_direction

        new_head = head + self.direction
        self.body.insert(0, new_head)
        self.body.pop()

    def is_valid_direction(self, direction):
        new_head = self.body[0] + direction
        if new_head in self.body[1:] or \
                new_head.x < 1 or new_head.x >= settings.GRID_WIDTH - 1 or \
                new_head.y < 2 or new_head.y >= settings.GRID_HEIGHT - 1:
            return False

        return True

    def find_next_valid_direction(self):
        directions = [Vector2(1, 0), Vector2(-1, 0), Vector2(0, 1), Vector2(0, -1)]

        for direction in directions:
            if self.is_valid_direction(direction):
                return direction

        # If no valid direction is found, continue in the current direction
        return self.direction

    def move_towards_food(self, food_position):
        next_direction = Vector2(0, 0)
        if self.body[0].x < food_position[0]:
            next_direction = Vector2(1, 0)
        elif self.body[0].x > food_position[0]:
            next_direction = Vector2(-1, 0)
        elif self.body[0].y < food_position[1]:
            next_direction = Vector2(0, 1)
        elif self.body[0].y > food_position[1]:
            next_direction = Vector2(0, -1)
        return next_direction

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self, screen):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, segment in enumerate(self.body):
            block_rect = pygame.Rect(
                segment[0] * settings.GRID_SIZE,
                segment[1] * settings.GRID_SIZE,
                settings.GRID_SIZE,
                settings.GRID_SIZE
            )

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
        if (
            self.body[0][0] < 1 or
            self.body[0][0] >= settings.GRID_WIDTH - 1 or
            self.body[0][1] < 2 or
            self.body[0][1] >= settings.GRID_HEIGHT - 1
        ):
            return True
        for segment in self.body[1:]:
            if segment == self.body[0]:
                return True
        return False


class Food:
    def __init__(self, snake_position):
        self.position = self.generate_position(snake_position)

    def generate_position(self, snake_position):
        while True:
            new_position = (randint(1, settings.GRID_WIDTH - 2), randint(2, settings.GRID_HEIGHT - 2))
            if new_position not in snake_position.body:
                return new_position

    def draw(self, screen):
        screen.blit(graphics.frame_food, pygame.Rect((self.position[0] * settings.GRID_SIZE), (self.position[1] * settings.GRID_SIZE), settings.GRID_SIZE, settings.GRID_SIZE))




class Food:
    def __init__(self, snake_position):
        self.position = self.generate_position(snake_position)

    def generate_position(self, snake_position):
        while True:
            new_position = (randint(1, settings.GRID_WIDTH - 2), randint(2, settings.GRID_HEIGHT - 2))
            if new_position not in snake_position.body:
                return new_position

    def draw(self, screen):
        screen.blit(graphics.frame_food, pygame.Rect((self.position[0] * settings.GRID_SIZE), (self.position[1] * settings.GRID_SIZE), settings.GRID_SIZE, settings.GRID_SIZE))


class Leaderboard:
    def __init__(self):
        self.scores = []

    def add_score(self, player_name, score):
        self.scores.append((player_name, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)  # Sort the scores in descending order

    def get_leaderboard_text(self):
        leaderboard_text = "LEADERBOARD\n\n"
        for index, (player_name, score) in enumerate(self.scores, start=1):
            leaderboard_text += f"{index}. {player_name}: {score}\n"
        return leaderboard_text
