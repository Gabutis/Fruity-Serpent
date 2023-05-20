import pygame
import sys
import settings
import klases
import graphics


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption('Baigiamasis Gyvatukas')

snake = klases.Snake()
food = klases.Food(snake)

sound_bite = pygame.mixer.Sound("Bite.mp3")
sound_background = pygame.mixer.music.load("background_sound.mp3")
pygame.mixer.music.play()

game_state = settings.MENU

clock = pygame.time.Clock()


def is_button_clicked(rect, pos):
    if rect.collidepoint(pos):
        return True
    return False

auto_move = False

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
                checkbox_rect = checkbox.get_rect(topright=(settings.WIDTH - settings.GRID_SIZE - 10, settings.GRID_SIZE + 10))
                if is_button_clicked(start_button_rect, pos):
                    game_state = settings.GAME
                if is_button_clicked(exit_button_rect, pos):
                    pygame.quit()
                    sys.exit()
                if is_button_clicked(checkbox_rect, pos):
                    auto_move = not auto_move
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
        if auto_move:
            snake.move_towards_food(food.position)
            snake.move(food.position, auto_move=True)
        else:
            snake.move(food.position)

        if snake.check_collision():
            game_state = settings.MENU
            snake = klases.Snake()
            food = klases.Food(snake)

        if snake.body[0] == food.position:
            sound_bite.play()
            snake.grow()
            food.position = food.generate_position(snake)

    screen.blit(graphics.background, (0, 0))

    if game_state == settings.MENU:
        title_text, start_button, exit_button, checkbox, checkbox_rect = graphics.game_state_menu(auto_move)
    elif game_state == settings.GAME:
        snake.draw(screen)
        food.draw(screen)
        graphics.game_state_game()

    pygame.display.flip()
    clock.tick(60)
