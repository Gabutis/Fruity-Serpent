from classes import snake, food, superfood, leaderboard
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
pygame.display.set_caption("Fruity Serpent")

serpent1 = snake.Snake()
food = food.Food(serpent1)
superfood = superfood.SuperFood()

leaderboard_game = leaderboard.Leaderboard.load_leaderboard()
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
                    if not serpent1.auto_move:
                        game_state = settings.NAME_INPUT
                    else:
                        game_state = settings.GAME
                if exit_button_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button_rect.collidepoint(pos):
                    game_state = settings.LEADERBOARD
                if checkbox_rect.collidepoint(pos):
                    serpent1.auto_move = not serpent1.auto_move

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not serpent1.auto_move:
                    game_state = settings.NAME_INPUT
                else:
                    game_state = settings.GAME

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                game_state = settings.LEADERBOARD

        elif game_state == settings.GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and serpent1.direction != (0, 1):
                    serpent1.direction = (0, -1)
                elif event.key == pygame.K_s and serpent1.direction != (0, -1):
                    serpent1.direction = (0, 1)
                elif event.key == pygame.K_a and serpent1.direction != (1, 0):
                    serpent1.direction = (-1, 0)
                elif event.key == pygame.K_d and serpent1.direction != (-1, 0):
                    serpent1.direction = (1, 0)

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
                    if serpent1.player_name:
                        serpent1.player_name = serpent1.player_name[:-1]
                        last_player_name = last_player_name[:-1]
                elif event.unicode.isprintable():
                    if last_player_name != "":
                        last_player_name = ""
                        serpent1.player_name = ""
                    serpent1.player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                input_text, input_text_position = graphics.game_state_name_input(
                    serpent1.player_name
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
        if serpent1.auto_move:
            if superfood.position is not None:
                serpent1.move_towards_food(superfood.position)
                serpent1.move(superfood.position, auto_move=True)
            else:
                serpent1.move_towards_food(food.position)
                serpent1.move(food.position, auto_move=True)
        else:
            serpent1.move(food.position)

        if serpent1.check_collision():
            sounds.sound_collision.play()
            superfood.position = None
            game_state = settings.MENU
            leaderboard_game.add_score(serpent1.player_name, serpent1.score)
            leaderboard.Leaderboard.save_leaderboard(leaderboard_game)
            last_player_name = serpent1.player_name
            serpent1 = snake.Snake()

        if serpent1.body[0] == food.position:
            sounds.sound_bite.play()
            serpent1.score += 1
            serpent1.grow()
            food.position = food.generate_position(serpent1)
            if superfood.position is None:
                superfood.food_spawns += 1
                superfood.update(serpent1)
            else:
                superfood.draw(screen)

        if serpent1.body[0] == superfood.position:
            sounds.sound_bite.play()
            serpent1.score += 2
            serpent1.body.pop()
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
        ) = graphics.game_state_menu(serpent1.auto_move)
    elif game_state == settings.NAME_INPUT:
        if last_player_name != "":
            serpent1.player_name = last_player_name
        graphics.game_state_name_input(serpent1.player_name)
    elif game_state == settings.GAME:
        serpent1.draw(screen)
        food.draw(screen)
        superfood.draw(screen)
        graphics.game_state_game(serpent1.player_name, serpent1.score, serpent1.auto_move)
    elif game_state == settings.LEADERBOARD:
        leaderboard_game = leaderboard.Leaderboard.load_leaderboard()
        back_text_position, back_text = graphics.game_state_leaderboard(leaderboard_game)
        graphics.game_state_leaderboard(leaderboard_game)

    pygame.display.flip()
    clock.tick(15)
