from classes import Snake, Food, SuperFood, Leaderboard
import sounds
import settings
import graphics
import pygame
import sys


pygame.init()
pygame.mixer.init()

sounds.pygame.mixer.music.play()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Baigiamasis Gyvatukas")

snake = Snake.Snake()
food = Food.Food(snake)
superfood = SuperFood.SuperFood()

leaderboard = Leaderboard.Leaderboard.load_leaderboard()
last_player_name = ""

game_state = settings.MENU

start_button = None
leaderboard_button = None
exit_button = None
checkbox = None
back_text = None

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
                start_button_rect = start_button.get_rect(
                    topleft=(
                        settings.WIDTH // 2 - start_button.get_width() // 2,
                        settings.HEIGHT // 2 - 50,
                    )
                )
                leaderboard_button_rect = leaderboard_button.get_rect(
                    topleft=(
                        settings.WIDTH // 2 - leaderboard_button.get_width() // 2,
                        settings.HEIGHT // 2,
                    )
                )
                exit_button_rect = exit_button.get_rect(
                    topleft=(
                        settings.WIDTH // 2 - exit_button.get_width() // 2,
                        settings.HEIGHT - 50,
                    )
                )
                checkbox_rect = checkbox.get_rect(
                    topright=(
                        settings.WIDTH - settings.GRID_SIZE - 10,
                        settings.GRID_SIZE + 10,
                    )
                )
                if start_button_rect.collidepoint(pos):
                    if not snake.auto_move:
                        game_state = settings.NAME_INPUT
                    else:
                        game_state = settings.GAME
                if exit_button_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button_rect.collidepoint(pos):
                    game_state = settings.LEADERBOARD
                if checkbox_rect.collidepoint(pos):
                    snake.auto_move = not snake.auto_move

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not snake.auto_move:
                    game_state = settings.NAME_INPUT
                else:
                    game_state = settings.GAME

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                game_state = settings.LEADERBOARD

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

        elif game_state == settings.LEADERBOARD:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                game_state = settings.MENU
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                back_text_rect = back_text.get_rect(
                    topleft=(
                        settings.WIDTH // 2 - back_text.get_width() // 2,
                        settings.HEIGHT - 50,
                    )
                )
                if back_text_rect.collidepoint(pos):
                    game_state = settings.MENU

        elif game_state == settings.NAME_INPUT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    game_state = settings.GAME
                elif event.key == pygame.K_BACKSPACE:
                    if snake.player_name:
                        snake.player_name = snake.player_name[:-1]
                        last_player_name = last_player_name[:-1]
                elif event.unicode.isprintable():
                    if last_player_name != "":
                        last_player_name = ""
                        snake.player_name = ""
                    snake.player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                input_text, input_text_position = graphics.game_state_name_input(
                    snake.player_name
                )
                click_rect = pygame.Rect(
                    input_text_position[0],
                    input_text_position[1],
                    input_text.get_width(),
                    input_text.get_height(),
                )
                if click_rect.collidepoint(pos):
                    game_state = settings.GAME

    if game_state == settings.GAME:
        if snake.auto_move:
            if superfood.position is not None:
                snake.move_towards_food(superfood.position)
                snake.move(superfood.position, auto_move=True)
            else:
                snake.move_towards_food(food.position)
                snake.move(food.position, auto_move=True)
        else:
            snake.move(food.position)

        if snake.check_collision():
            sounds.sound_collision.play()
            superfood.position = None
            game_state = settings.MENU
            leaderboard.add_score(snake.player_name, snake.score)
            Leaderboard.Leaderboard.save_leaderboard(leaderboard)
            last_player_name = snake.player_name
            snake = Snake.Snake()

        if snake.body[0] == food.position:
            sounds.sound_bite.play()
            snake.score += 1
            snake.grow()
            food.position = food.generate_position(snake)
            if superfood.position is None:
                superfood.food_spawns += 1
                superfood.update(snake)
            else:
                superfood.draw(screen)

        if snake.body[0] == superfood.position:
            sounds.sound_bite.play()
            snake.score += 2
            snake.body.pop()
            superfood.position = None
            superfood.timer = 0

    screen.blit(graphics.background, (0, 0))

    if game_state == settings.MENU:
        (
            title_text,
            start_button,
            leaderboard_button,
            exit_button,
            checkbox,
            checkbox_rect,
        ) = graphics.game_state_menu(snake.auto_move)
    elif game_state == settings.NAME_INPUT:
        if last_player_name != "":
            snake.player_name = last_player_name
        graphics.game_state_name_input(snake.player_name)
    elif game_state == settings.GAME:
        snake.draw(screen)
        food.draw(screen)
        superfood.draw(screen)
        graphics.game_state_game(snake.player_name, snake.score, snake.auto_move)
    elif game_state == settings.LEADERBOARD:
        leaderboard = Leaderboard.Leaderboard.load_leaderboard()
        back_text_position, back_text = graphics.game_state_leaderboard(leaderboard)
        graphics.game_state_leaderboard(leaderboard)

    pygame.display.flip()
    clock.tick(15)
