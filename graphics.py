import settings
import pygame


def get_image(sheet, frame_w, frame_h, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame_w * width), (frame_h * height), width, height))
    image = pygame.transform.scale(
        image, (scale * settings.GRID_SIZE, scale * settings.GRID_SIZE)
    )
    image.set_colorkey(color)
    return image


pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("pictures/background.jpg")
background = pygame.transform.scale(background, (settings.WIDTH, settings.HEIGHT))

snake_sprite = pygame.image.load("pictures/snake_sprite.png")

frame_btr = get_image(snake_sprite, 0, 0, 64, 64, 1, settings.BLACK).convert_alpha()
frame_btl = get_image(snake_sprite, 2, 0, 64, 64, 1, settings.BLACK).convert_alpha()
frame_bbr = get_image(snake_sprite, 0, 1, 64, 64, 1, settings.BLACK).convert_alpha()
frame_bbl = get_image(snake_sprite, 2, 2, 64, 64, 1, settings.BLACK).convert_alpha()

frame_bh = get_image(snake_sprite, 1, 0, 64, 64, 1, settings.BLACK).convert_alpha()
frame_bv = get_image(snake_sprite, 2, 1, 64, 64, 1, settings.BLACK).convert_alpha()

frame_hr = get_image(snake_sprite, 4, 0, 64, 64, 1, settings.BLACK).convert_alpha()
frame_hl = get_image(snake_sprite, 3, 1, 64, 64, 1, settings.BLACK).convert_alpha()
frame_ht = get_image(snake_sprite, 3, 0, 64, 64, 1, settings.BLACK).convert_alpha()
frame_hb = get_image(snake_sprite, 4, 1, 64, 64, 1, settings.BLACK).convert_alpha()

frame_tr = get_image(snake_sprite, 3, 3, 64, 64, 1, settings.BLACK).convert_alpha()
frame_tl = get_image(snake_sprite, 4, 2, 64, 64, 1, settings.BLACK).convert_alpha()
frame_tt = get_image(snake_sprite, 4, 3, 64, 64, 1, settings.BLACK).convert_alpha()
frame_tb = get_image(snake_sprite, 3, 2, 64, 64, 1, settings.BLACK).convert_alpha()

frame_food = get_image(snake_sprite, 0, 3, 66, 64, 1, settings.BLACK).convert_alpha()

banana_sprite = pygame.image.load("pictures/banana.png")

frame_superfood0 = get_image(
    banana_sprite, 0, 0, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood1 = get_image(
    banana_sprite, 1, 0, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood2 = get_image(
    banana_sprite, 2, 0, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood3 = get_image(
    banana_sprite, 3, 0, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood4 = get_image(
    banana_sprite, 0, 1, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood5 = get_image(
    banana_sprite, 1, 1, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood6 = get_image(
    banana_sprite, 2, 1, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()
frame_superfood7 = get_image(
    banana_sprite, 3, 1, 546.5, 546.5, 1, settings.BLACK
).convert_alpha()


def game_state_menu(auto_move):
    menu_font = pygame.font.Font(None, 36)

    title_text_border = menu_font.render("Baigiamasis Gyvatukas", True, settings.GREEN)
    title_text = menu_font.render("Baigiamasis Gyvatukas", True, settings.PURPLE)
    title_text_position = (
        settings.WIDTH // 2 - title_text.get_width() // 2,
        settings.HEIGHT // 2 - 250,
    )

    start_button_border = menu_font.render(
        "Press SPACE or click to start", True, settings.GREEN
    )
    start_button = menu_font.render(
        "Press SPACE or click to start", True, settings.PURPLE
    )
    leaderboard_button_border = menu_font.render(
        "Press L or click for Leaderboard", True, settings.GREEN
    )
    leaderboard_button = menu_font.render(
        "Press L or click for Leaderboard", True, settings.PURPLE
    )
    exit_button_border = menu_font.render(
        "Press ESC or click to EXIT", True, settings.GREEN
    )
    exit_button = menu_font.render("Press ESC or click to EXIT", True, settings.PURPLE)

    checkbox_label_border = menu_font.render("Auto Move", True, settings.GREEN)
    checkbox_label = menu_font.render("Auto Move", True, settings.PURPLE)
    checkbox = pygame.Surface((20, 20))
    checkbox.fill(settings.PURPLE if auto_move else settings.WHITE)
    checkbox_rect = checkbox.get_rect(
        topright=(settings.WIDTH - settings.GRID_SIZE - 10, settings.GRID_SIZE + 10)
    )

    screen.blit(title_text_border, (title_text_position[0] - 2, title_text_position[1]))
    screen.blit(title_text_border, (title_text_position[0] + 2, title_text_position[1]))
    screen.blit(title_text_border, (title_text_position[0], title_text_position[1] - 2))
    screen.blit(title_text_border, (title_text_position[0], title_text_position[1] + 2))
    screen.blit(title_text, title_text_position)

    screen.blit(
        start_button_border,
        (
            settings.WIDTH // 2 - start_button.get_width() // 2 - 2,
            settings.HEIGHT // 2 - 50,
        ),
    )
    screen.blit(
        start_button_border,
        (
            settings.WIDTH // 2 - start_button.get_width() // 2 + 2,
            settings.HEIGHT // 2 - 50,
        ),
    )
    screen.blit(
        start_button_border,
        (
            settings.WIDTH // 2 - start_button.get_width() // 2,
            settings.HEIGHT // 2 - 2 - 50,
        ),
    )
    screen.blit(
        start_button_border,
        (
            settings.WIDTH // 2 - start_button.get_width() // 2,
            settings.HEIGHT // 2 + 2 - 50,
        ),
    )
    screen.blit(
        start_button,
        (
            settings.WIDTH // 2 - start_button.get_width() // 2,
            settings.HEIGHT // 2 - 50,
        ),
    )

    screen.blit(
        leaderboard_button_border,
        (
            settings.WIDTH // 2 - leaderboard_button.get_width() // 2 - 2,
            settings.HEIGHT // 2,
        ),
    )
    screen.blit(
        leaderboard_button_border,
        (
            settings.WIDTH // 2 - leaderboard_button.get_width() // 2 + 2,
            settings.HEIGHT // 2,
        ),
    )
    screen.blit(
        leaderboard_button_border,
        (
            settings.WIDTH // 2 - leaderboard_button.get_width() // 2,
            settings.HEIGHT // 2 - 2,
        ),
    )
    screen.blit(
        leaderboard_button_border,
        (
            settings.WIDTH // 2 - leaderboard_button.get_width() // 2,
            settings.HEIGHT // 2 + 2,
        ),
    )
    screen.blit(
        leaderboard_button,
        (
            settings.WIDTH // 2 - leaderboard_button.get_width() // 2,
            settings.HEIGHT // 2,
        ),
    )

    screen.blit(
        exit_button_border,
        (settings.WIDTH // 2 - exit_button.get_width() // 2 - 2, settings.HEIGHT - 50),
    )
    screen.blit(
        exit_button_border,
        (settings.WIDTH // 2 - exit_button.get_width() // 2 + 2, settings.HEIGHT - 50),
    )
    screen.blit(
        exit_button_border,
        (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT - 50 - 2),
    )
    screen.blit(
        exit_button_border,
        (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT - 50 + 2),
    )
    screen.blit(
        exit_button,
        (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT - 50),
    )

    screen.blit(
        checkbox_label_border,
        (checkbox_rect.left - checkbox_label.get_width() - 10 - 2, checkbox_rect.top),
    )
    screen.blit(
        checkbox_label_border,
        (checkbox_rect.left - checkbox_label.get_width() - 10 + 2, checkbox_rect.top),
    )
    screen.blit(
        checkbox_label_border,
        (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top - 2),
    )
    screen.blit(
        checkbox_label_border,
        (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top + 2),
    )
    screen.blit(
        checkbox_label,
        (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top),
    )
    screen.blit(checkbox, checkbox_rect)

    return (
        title_text,
        start_button,
        leaderboard_button,
        exit_button,
        checkbox,
        checkbox_rect,
    )


def game_state_name_input(player_name):
    input_font = pygame.font.Font(None, 36)

    input_text_border = input_font.render(
        "Enter your name and press SPACE or click to start:", True, settings.GREEN
    )
    input_text = input_font.render(
        "Enter your name and press SPACE or click to start:", True, settings.PURPLE
    )
    input_text_position = (
        settings.WIDTH // 2 - input_text.get_width() // 2,
        settings.HEIGHT // 2 - 50,
    )

    player_name_text_border = input_font.render(player_name, True, settings.PURPLE)
    player_name_text = input_font.render(player_name, True, settings.GREEN)
    player_name_text_position = (
        settings.WIDTH // 2 - player_name_text.get_width() // 2,
        settings.HEIGHT // 2,
    )

    screen.blit(input_text_border, (input_text_position[0] - 2, input_text_position[1]))
    screen.blit(input_text_border, (input_text_position[0] + 2, input_text_position[1]))
    screen.blit(input_text_border, (input_text_position[0], input_text_position[1] - 2))
    screen.blit(input_text_border, (input_text_position[0], input_text_position[1] + 2))
    screen.blit(input_text, input_text_position)

    screen.blit(
        player_name_text_border,
        (player_name_text_position[0] - 2, player_name_text_position[1]),
    )
    screen.blit(
        player_name_text_border,
        (player_name_text_position[0] + 2, player_name_text_position[1]),
    )
    screen.blit(
        player_name_text_border,
        (player_name_text_position[0], player_name_text_position[1] - 2),
    )
    screen.blit(
        player_name_text_border,
        (player_name_text_position[0], player_name_text_position[1] + 2),
    )
    screen.blit(player_name_text, player_name_text_position)

    return input_text, input_text_position


def game_state_game(player_name, score, auto_move):
    pygame.draw.rect(
        screen, settings.GREY, (0, 0, settings.WIDTH, settings.GRID_SIZE * 2)
    )
    pygame.draw.rect(
        screen,
        settings.GREY,
        (0, settings.HEIGHT - settings.GRID_SIZE, settings.WIDTH, settings.GRID_SIZE),
    )
    pygame.draw.rect(screen, settings.GREY, (0, 0, settings.GRID_SIZE, settings.HEIGHT))
    pygame.draw.rect(
        screen,
        settings.GREY,
        (settings.WIDTH - settings.GRID_SIZE, 0, settings.GRID_SIZE, settings.HEIGHT),
    )

    font = pygame.font.Font(None, 36)
    name_text_border = font.render(f"Player: {player_name}", True, settings.GREEN)
    name_text = font.render(f"Player: {player_name}", True, settings.PURPLE)
    score_text_border = font.render(f"Score: {score}", True, settings.GREEN)
    score_text = font.render(f"Score: {score}", True, settings.PURPLE)

    screen.blit(
        score_text_border, (settings.GRID_SIZE / 2 - 2, settings.GRID_SIZE / 2 - 2)
    )
    screen.blit(
        score_text_border, (settings.GRID_SIZE / 2 + 2, settings.GRID_SIZE / 2 - 2)
    )
    screen.blit(
        score_text_border, (settings.GRID_SIZE / 2 - 2, settings.GRID_SIZE / 2 + 2)
    )
    screen.blit(
        score_text_border, (settings.GRID_SIZE / 2 + 2, settings.GRID_SIZE / 2 + 2)
    )
    screen.blit(score_text, (settings.GRID_SIZE / 2, settings.GRID_SIZE / 2))

    if player_name and not auto_move:
        screen.blit(
            name_text_border, (settings.GRID_SIZE * 8, settings.GRID_SIZE / 2 - 2)
        )
        screen.blit(
            name_text_border, (settings.GRID_SIZE * 8 + 2, settings.GRID_SIZE / 2 - 2)
        )
        screen.blit(
            name_text_border, (settings.GRID_SIZE * 8 - 2, settings.GRID_SIZE / 2 + 2)
        )
        screen.blit(
            name_text_border, (settings.GRID_SIZE * 8 + 2, settings.GRID_SIZE / 2 + 2)
        )
        screen.blit(name_text, (settings.GRID_SIZE * 8, settings.GRID_SIZE / 2))


def game_state_leaderboard(leaderboard):
    title_font = pygame.font.Font(None, 50)
    entry_font = pygame.font.Font(None, 36)
    back_text_font = pygame.font.Font(None, 36)

    title_text_border = title_font.render("LEADERBOARD", True, settings.GREEN)
    title_text = title_font.render("LEADERBOARD", True, settings.PURPLE)
    back_text_border = back_text_font.render(
        "Press L or click to go back", True, settings.GREEN
    )
    back_text = back_text_font.render(
        "Press L or click to go back", True, settings.PURPLE
    )
    title_text_position = (settings.WIDTH // 2 - title_text.get_width() // 2, 50)
    back_text_position = (
        settings.WIDTH // 2 - back_text.get_width() // 2,
        settings.HEIGHT - 50,
    )

    screen.blit(title_text_border, (title_text_position[0] - 2, title_text_position[1]))
    screen.blit(title_text_border, (title_text_position[0] + 2, title_text_position[1]))
    screen.blit(title_text_border, (title_text_position[0], title_text_position[1] - 2))
    screen.blit(title_text_border, (title_text_position[0], title_text_position[1] + 2))
    screen.blit(title_text, title_text_position)

    screen.blit(back_text_border, (back_text_position[0] - 2, back_text_position[1]))
    screen.blit(back_text_border, (back_text_position[0] + 2, back_text_position[1]))
    screen.blit(back_text_border, (back_text_position[0], back_text_position[1] - 2))
    screen.blit(back_text_border, (back_text_position[0], back_text_position[1] + 2))
    screen.blit(back_text, back_text_position)

    sorted_entries = sorted(
        leaderboard.entries, key=lambda entry: entry.score, reverse=True
    )

    for i, entry in enumerate(sorted_entries):
        player_name = entry.player_name
        score = entry.score

        entry_text = f"{player_name}: {score}"
        entry_text_border = entry_font.render(entry_text, True, settings.GREEN)
        entry_surface = entry_font.render(entry_text, True, settings.PURPLE)

        entry_rect = entry_text_border.get_rect(
            midtop=(settings.WIDTH // 2, 100 + i * 30)
        )
        screen.blit(entry_text_border, entry_rect.move(-2, 0))
        screen.blit(entry_text_border, entry_rect.move(2, 0))
        screen.blit(entry_text_border, entry_rect.move(0, -2))
        screen.blit(entry_text_border, entry_rect.move(0, 2))
        screen.blit(entry_surface, entry_rect)

    return back_text_position, back_text
