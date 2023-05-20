import pygame
import sys
import settings
import klases
import graphics


pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption('Baigiamasis Gyvatukas')

snake = klases.Snake()
food = klases.Food(snake)

game_state = settings.MENU

clock = pygame.time.Clock()

menu_font = pygame.font.Font(None, 36)

def is_button_clicked(rect, pos):
    if rect.collidepoint(pos):
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if game_state == settings.MENU:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                start_button_rect = start_button.get_rect(topleft=(settings.WIDTH // 2 - start_button.get_width() // 2, settings.HEIGHT // 2 + 50))
                exit_button_rect = exit_button.get_rect(topleft=(settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT // 2 + 100))
                if is_button_clicked(start_button_rect, pos):
                    game_state = settings.GAME
                if is_button_clicked(exit_button_rect, pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = settings.GAME
        elif game_state == settings.GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_s and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_a and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_d and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

    if game_state == settings.GAME:
        snake.move()

        if snake.check_collision():
            game_state = settings.MENU
            snake = klases.Snake()
            food = klases.Food(snake)

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.generate_position(snake)

    screen.blit(graphics.background, (0, 0))

    if game_state == settings.MENU:
        title_text = menu_font.render("Snake Game", True, settings.PURPLE)
        screen.blit(title_text, (settings.WIDTH // 2 - title_text.get_width() // 2, settings.HEIGHT // 2 - 100))
        start_button = menu_font.render("Press SPACE or click to start", True, settings.PURPLE)
        screen.blit(start_button, (settings.WIDTH // 2 - start_button.get_width() // 2, settings.HEIGHT // 2 + 50))
        exit_button = menu_font.render("Press ESC or click to EXIT", True, settings.PURPLE)
        screen.blit(exit_button, (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT // 2 + 100))
    elif game_state == settings.GAME:
        snake.draw(screen)
        food.draw(screen)
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.WIDTH, settings.GRID_SIZE * 2))
        pygame.draw.rect(screen, settings.GREY, (0, settings.HEIGHT - settings.GRID_SIZE, settings.WIDTH, settings.GRID_SIZE))
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.GRID_SIZE, settings.HEIGHT))
        pygame.draw.rect(screen, settings.GREY, (settings.WIDTH - settings.GRID_SIZE, 0, settings.GRID_SIZE, settings.HEIGHT))

    pygame.display.flip()
    clock.tick(10)
