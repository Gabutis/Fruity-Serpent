import pygame
import sys
import settings
import klases

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption('Baigiamasis Gyvatukas')

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (settings.WIDTH, settings.HEIGHT))

snake = klases.Snake()
food = klases.Food()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_s and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key == pygame.K_a and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_d and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    snake.move()

    if snake.check_collision():
        pygame.quit()
        sys.exit()

    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.generate_position()

    screen.blit(background, (0, 0))
    snake.draw(screen)
    food.draw(screen)
    pygame.draw.rect(screen, settings.GREY, (0, 0, settings.WIDTH, settings.GRID_SIZE * 2))
    pygame.draw.rect(screen, settings.GREY, (0, settings.HEIGHT - settings.GRID_SIZE, settings.WIDTH, settings.GRID_SIZE))
    pygame.draw.rect(screen, settings.GREY, (0, 0, settings.GRID_SIZE, settings.HEIGHT))
    pygame.draw.rect(screen, settings.GREY, (settings.WIDTH - settings.GRID_SIZE, 0, settings.GRID_SIZE, settings.HEIGHT))
    pygame.display.flip()
    clock.tick(10)
