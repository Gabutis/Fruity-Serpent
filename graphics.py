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


def draw_text_with_border(text, offset=0, text_position=None, font=36, highlight_on_mouse=True):
    text_font = pygame.font.Font(None, font)
    text_inner = text_font.render(text, True, settings.PURPLE)
    text_outer = text_font.render(text, True, settings.GREEN)

    if text_position is None:
        text_position = (settings.WIDTH // 2 - text_inner.get_width() // 2, settings.HEIGHT // 2 - offset)

    outer_rect = text_outer.get_rect(topleft=text_position)

    if highlight_on_mouse and outer_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(text_outer, (text_position[0] - 2, text_position[1]))
        screen.blit(text_outer, (text_position[0] + 2, text_position[1]))
        screen.blit(text_outer, (text_position[0], text_position[1] - 2))
        screen.blit(text_outer, (text_position[0], text_position[1] + 2))
    elif not highlight_on_mouse:
        screen.blit(text_outer, (text_position[0] - 2, text_position[1]))
        screen.blit(text_outer, (text_position[0] + 2, text_position[1]))
        screen.blit(text_outer, (text_position[0], text_position[1] - 2))
        screen.blit(text_outer, (text_position[0], text_position[1] + 2))

    screen.blit(text_inner, text_inner.get_rect(topleft=text_position))

    return outer_rect


def draw_checkbox_with_text(text, text_position=None, checked=False, font=36, highlight_on_mouse=False):
    checkbox_size = 20
    checkbox_padding = 5
    text_font = pygame.font.Font(None, font)
    text_inner = text_font.render(text, True, settings.PURPLE)
    text_outer = text_font.render(text, True, settings.GREEN)
    text_rect = text_inner.get_rect()

    if text_position is None:
        text_position = (
        settings.WIDTH // 2 - (checkbox_size + checkbox_padding + text_rect.width) // 2, settings.HEIGHT // 2)

    checkbox_rect = pygame.Rect(text_position[0], text_position[1], checkbox_size, checkbox_size)
    text_rect.topleft = (text_position[0] + checkbox_size + checkbox_padding, text_position[1])

    if checked:
        pygame.draw.rect(screen, settings.GREEN, checkbox_rect)
        pygame.draw.rect(screen, settings.PURPLE, checkbox_rect, 2)
    else:
        pygame.draw.rect(screen, settings.PURPLE, checkbox_rect, 2)

    if highlight_on_mouse and (
            checkbox_rect.collidepoint(pygame.mouse.get_pos()) or text_rect.collidepoint(pygame.mouse.get_pos())):
        screen.blit(text_outer, (text_rect.left - 2, text_rect.top))
        screen.blit(text_outer, (text_rect.left + 2, text_rect.top))
        screen.blit(text_outer, (text_rect.left, text_rect.top - 2))
        screen.blit(text_outer, (text_rect.left, text_rect.top + 2))
    elif not highlight_on_mouse:
        screen.blit(text_outer, (text_rect.left - 2, text_rect.top))
        screen.blit(text_outer, (text_rect.left + 2, text_rect.top))
        screen.blit(text_outer, (text_rect.left, text_rect.top - 2))
        screen.blit(text_outer, (text_rect.left, text_rect.top + 2))

    screen.blit(text_inner, text_rect.topleft)

    return checkbox_rect, text_rect


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


def game_state_game():
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


def game_state_leaderboard(leaderboard):
    font = pygame.font.Font(None, 36)

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

    return
