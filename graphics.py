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


def draw_text_with_border(text, position=0, font=36):
    text_font = pygame.font.Font(None, font)
    text_outer = text_font.render(text, True, settings.GREEN)
    text_inner = text_font.render(text, True, settings.PURPLE)
    text_position = (settings.WIDTH // 2 - text_inner.get_width() // 2, settings.HEIGHT // 2 - position)
    screen.blit(text_outer, (text_position[0] - 2, text_position[1]))
    screen.blit(text_outer, (text_position[0] + 2, text_position[1]))
    screen.blit(text_outer, (text_position[0], text_position[1] - 2))
    screen.blit(text_outer, (text_position[0], text_position[1] + 2))
    screen.blit(text_inner, text_position)


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.RESIZABLE)

icon_image = pygame.image.load("pictures/icon_for_game.png")
pygame.display.set_icon(icon_image)

menu_background = pygame.image.load("pictures/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background, (settings.WIDTH, settings.HEIGHT))

game_background = pygame.image.load("pictures/game_background.jpg")
game_background = pygame.transform.scale(game_background, (settings.WIDTH, settings.HEIGHT))

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

    draw_text_with_border("Fruity Serpent", 250)
    draw_text_with_border("Press SPACE or click to start", 50)
    start_button = menu_font.render(
        "Press SPACE or click to start", True, settings.PURPLE
    )
    draw_text_with_border("Press L or click for Leaderboard")
    leaderboard_button = menu_font.render(
        "Press L or click for Leaderboard", True, settings.PURPLE
    )
    draw_text_with_border("Press S or click for Settings", -50)
    settings_button = menu_font.render(
        "Press S or click for Settings", True, settings.PURPLE
    )
    draw_text_with_border("Press ESC or click to EXIT", -250)
    exit_button = menu_font.render("Press ESC or click to EXIT", True, settings.PURPLE)

    checkbox_label_border = menu_font.render("Auto Move", True, settings.GREEN)
    checkbox_label = menu_font.render("Auto Move", True, settings.PURPLE)
    checkbox = pygame.Surface((20, 20))
    checkbox.fill(settings.PURPLE if auto_move else settings.WHITE)
    checkbox_rect = checkbox.get_rect(
        topright=(settings.WIDTH - settings.GRID_SIZE - 10, settings.GRID_SIZE + 10)
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
        start_button,
        leaderboard_button,
        settings_button,
        exit_button,
        checkbox,
        checkbox_rect,
    )


def game_state_name_input(player_name):
    font = pygame.font.Font(None, 36)

    draw_text_with_border(player_name)
    draw_text_with_border("Enter your name and press SPACE or click to start:", 50)
    input_text = font.render(
        "Enter your name and press SPACE or click to start:", True, settings.PURPLE
    )
    input_text_position = (
        settings.WIDTH // 2 - input_text.get_width() // 2,
        settings.HEIGHT // 2 - 50,
    )



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
    font = pygame.font.Font(None, 36)

    draw_text_with_border("LEADERBOARD", 250)
    draw_text_with_border("Press L or click to go back", -250)
    back_text = font.render(
        "Press L or click to go back", True, settings.PURPLE
    )

    sorted_entries = sorted(
        leaderboard.entries, key=lambda entry: entry.score, reverse=True
    )

    for i, entry in enumerate(sorted_entries):
        player_name = entry.player_name
        score = entry.score

        entry_text = f"{player_name}: {score}"
        entry_text_border = font.render(entry_text, True, settings.GREEN)
        entry_surface = font.render(entry_text, True, settings.PURPLE)

        entry_rect = entry_text_border.get_rect(
            midtop=(settings.WIDTH // 2, 100 + i * 30)
        )
        screen.blit(entry_text_border, entry_rect.move(-2, 0))
        screen.blit(entry_text_border, entry_rect.move(2, 0))
        screen.blit(entry_text_border, entry_rect.move(0, -2))
        screen.blit(entry_text_border, entry_rect.move(0, 2))
        screen.blit(entry_surface, entry_rect)

    return back_text


def game_state_settings():
    font = pygame.font.Font(None, 36)
    draw_text_with_border("SETTINGS", 250)
    draw_text_with_border("Press S or click to go back", -250)
    back_text = font.render(
        "Press S or click to go back", True, settings.PURPLE
    )

    return back_text
