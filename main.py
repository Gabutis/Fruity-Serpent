from classes import snake, food, superfood, leaderboard
import sounds
import settings
import graphics
import pygame
import sys


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Fruity Serpent")

serpent1 = snake.Snake()
food = food.Food(serpent1)
superfood = superfood.SuperFood()

sounds.pygame.mixer.music.play()
sound_slider = sounds.MusicSlider(100, 200, 20, 0, 10, "Music sound")
sounds.music_sound_volume = sound_slider.value / 10.0


leaderboard_game = leaderboard.Leaderboard.load_leaderboard()
last_player_name = ""

game_state = settings.MENU

start_button = None
leaderboard_button = None
settings_button = None
exit_button = None
auto_move_text_rect = None
auto_move_rect = None
auto_move_checked = False
leaderboard_back_text = None
settings_back_text = None
enter_name = None
name_imout_back_text = None
full_screen_rect = None
full_screen_text_rect = None
full_screen_checked = False
size = (settings.WIDTH, settings.HEIGHT)
dragging_slider = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            size = event.dict["size"]
            graphics.menu_background = pygame.transform.scale(
                graphics.menu_background, (event.w, event.h)
            )
            graphics.game_background = pygame.transform.scale(
                graphics.game_background, (event.w, event.h)
            )
            settings.GRID_WIDTH = event.w // settings.GRID_SIZE
            settings.GRID_HEIGHT = (event.h - settings.GRID_SIZE) // settings.GRID_SIZE
            settings.WIDTH = event.w
            settings.HEIGHT = event.h
            sound_slider.calculate_position(100)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if game_state == settings.MENU:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    if not serpent1.auto_move:
                        game_state = settings.NAME_INPUT
                    else:
                        game_state = settings.GAME
                if exit_button.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button.collidepoint(pos):
                    game_state = settings.LEADERBOARD
                if settings_button.collidepoint(pos):
                    game_state = settings.SETTINGS
                if auto_move_text_rect.collidepoint(pos) or auto_move_rect.collidepoint(
                    pos
                ):
                    auto_move_checked = not auto_move_checked
                    serpent1.auto_move = not serpent1.auto_move

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not serpent1.auto_move:
                    game_state = settings.NAME_INPUT
                else:
                    game_state = settings.GAME

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                game_state = settings.LEADERBOARD

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                game_state = settings.SETTINGS

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
                if leaderboard_back_text.collidepoint(pygame.mouse.get_pos()):
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if name_imout_back_text.collidepoint(pygame.mouse.get_pos()):
                    game_state = settings.MENU
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if enter_name.collidepoint(pygame.mouse.get_pos()):
                    game_state = settings.GAME

        elif game_state == settings.SETTINGS:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                game_state = settings.MENU
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sound_slider.rect.collidepoint(pygame.mouse.get_pos()):
                    dragging_slider = True
                if settings_back_text.collidepoint(pygame.mouse.get_pos()):
                    game_state = settings.MENU
                elif full_screen_rect.collidepoint(
                    pygame.mouse.get_pos()
                ) or full_screen_text_rect.collidepoint(pygame.mouse.get_pos()):
                    full_screen_checked = not full_screen_checked
                    if not full_screen_checked:
                        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    else:
                        modes = pygame.display.list_modes()
                        if modes:
                            max_mode = modes[0]
                            settings.WIDTH = max_mode[0]
                            settings.HEIGHT = max_mode[1]
                            settings.GRID_WIDTH = max_mode[0] // settings.GRID_SIZE
                            settings.GRID_HEIGHT = (
                                max_mode[1] - settings.GRID_SIZE
                            ) // settings.GRID_SIZE
                            screen = pygame.display.set_mode(
                                (settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN
                            )
                            graphics.menu_background = pygame.transform.scale(
                                graphics.menu_background, (max_mode[0], max_mode[1])
                            )
                            graphics.game_background = pygame.transform.scale(
                                graphics.game_background, (max_mode[0], max_mode[1])
                            )
                            sound_slider.calculate_position(100)
                        else:
                            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging_slider = False
            elif event.type == pygame.MOUSEMOTION and dragging_slider:
                sound_slider.update_value(event.pos[0])

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

    screen.blit(graphics.menu_background, (0, 0))

    if game_state == settings.MENU:
        graphics.draw_text_with_border(
            "Fruity Serpent", 250, font=70, highlight_on_mouse=False
        )
        auto_move_rect, auto_move_text_rect = graphics.draw_checkbox_with_text(
            "Auto move",
            0,
            (settings.WIDTH - (settings.GRID_SIZE * 5), settings.GRID_SIZE),
            auto_move_checked,
            highlight_on_mouse=True,
        )
        start_button = graphics.draw_text_with_border(
            "Press SPACE or click to start", 50
        )
        leaderboard_button = graphics.draw_text_with_border(
            "Press L or click for Leaderboard"
        )
        settings_button = graphics.draw_text_with_border(
            "Press S or click for Settings", -50
        )
        exit_button = graphics.draw_text_with_border("Press ESC or click to EXIT", -250)
    elif game_state == settings.NAME_INPUT:
        graphics.draw_text_with_border(serpent1.player_name, highlight_on_mouse=False)
        enter_name = graphics.draw_text_with_border(
            "Enter your name and press SPACE or click to start:", 50
        )
        if last_player_name != "":
            serpent1.player_name = last_player_name
        name_imout_back_text = graphics.draw_text_with_border("Click to go back", -250)
    elif game_state == settings.GAME:
        screen.blit(graphics.game_background, (0, 0))
        serpent1.draw(screen)
        food.draw(screen)
        superfood.draw(screen)
        graphics.game_state_game()
        graphics.draw_text_with_border(
            f"Score: {serpent1.score}",
            text_position=(settings.GRID_SIZE / 2, settings.GRID_SIZE / 2),
            highlight_on_mouse=False,
        )
        graphics.draw_text_with_border(
            serpent1.player_name,
            text_position=(settings.GRID_SIZE * 6, settings.GRID_SIZE / 2),
            highlight_on_mouse=False,
        )
    elif game_state == settings.LEADERBOARD:
        leaderboard_game = leaderboard.Leaderboard.load_leaderboard()
        graphics.draw_text_with_border(
            "LEADERBOARD", 250, font=70, highlight_on_mouse=False
        )
        leaderboard_back_text = graphics.draw_text_with_border(
            "Press L or click to go back", -250
        )
        graphics.game_state_leaderboard(leaderboard_game)
    elif game_state == settings.SETTINGS:
        graphics.draw_text_with_border(
            "SETTINGS", 250, font=70, highlight_on_mouse=False
        )
        full_screen_rect, full_screen_text_rect = graphics.draw_checkbox_with_text(
            "Fullscreen", 150, checked=full_screen_checked, highlight_on_mouse=True
        )
        settings_back_text = graphics.draw_text_with_border(
            "Press S or click to go back", -250
        )
        sound_slider.draw(screen)

    pygame.display.flip()
    clock.tick(15)
