import pygame
import settings


def get_image(sheet, frame_w, frame_h, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame_w * width), (frame_h * height), width, height))
    image = pygame.transform.scale(image, (scale * settings.GRID_SIZE, scale * settings.GRID_SIZE))
    image.set_colorkey(color)
    return image


pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (settings.WIDTH, settings.HEIGHT))

snake_sprite = pygame.image.load("snake_sprite.png").convert_alpha()

frame_btr = get_image(snake_sprite, 0, 0, 64, 64, 1, settings.BLACK)
frame_btl = get_image(snake_sprite, 2, 0, 64, 64, 1, settings.BLACK)
frame_bbr = get_image(snake_sprite, 0, 1, 64, 64, 1, settings.BLACK)
frame_bbl = get_image(snake_sprite, 2, 2, 64, 64, 1, settings.BLACK)

frame_bh = get_image(snake_sprite, 1, 0, 64, 64, 1, settings.BLACK)
frame_bv = get_image(snake_sprite, 2, 1, 64, 64, 1, settings.BLACK)

frame_hr = get_image(snake_sprite, 4, 0, 64, 64, 1, settings.BLACK)
frame_hl = get_image(snake_sprite, 3, 1, 64, 64, 1, settings.BLACK)
frame_ht = get_image(snake_sprite, 3, 0, 64, 64, 1, settings.BLACK)
frame_hb = get_image(snake_sprite, 4, 1, 64, 64, 1, settings.BLACK)

frame_tr = get_image(snake_sprite, 3, 3, 64, 64, 1, settings.BLACK)
frame_tl = get_image(snake_sprite, 4, 2, 64, 64, 1, settings.BLACK)
frame_tt = get_image(snake_sprite, 4, 3, 64, 64, 1, settings.BLACK)
frame_tb = get_image(snake_sprite, 3, 2, 64, 64, 1, settings.BLACK)

frame_food = get_image(snake_sprite, 0, 3, 66, 64, 1, settings.BLACK)

def game_state_menu(auto_move):
        menu_font = pygame.font.Font(None, 36)

        title_text_border = menu_font.render("Snake Game", True, settings.GREEN)
        title_text = menu_font.render("Snake Game", True, settings.PURPLE)
        title_text_position = (settings.WIDTH // 2 - title_text.get_width() // 2, settings.HEIGHT // 2 - 250)

        start_button_border = menu_font.render("Press SPACE or click to start", True, settings.GREEN)
        start_button = menu_font.render("Press SPACE or click to start", True, settings.PURPLE)
        exit_button_border = menu_font.render("Press ESC or click to EXIT", True, settings.GREEN)
        exit_button = menu_font.render("Press ESC or click to EXIT", True, settings.PURPLE)

        checkbox_label_border = menu_font.render("Auto Move", True, settings.GREEN)
        checkbox_label = menu_font.render("Auto Move", True, settings.PURPLE)
        checkbox = pygame.Surface((20, 20))
        checkbox.fill(settings.PURPLE if auto_move else settings.WHITE)
        checkbox_rect = checkbox.get_rect(topright=(settings.WIDTH - settings.GRID_SIZE - 10, settings.GRID_SIZE + 10))

        screen.blit(title_text_border, (title_text_position[0] - 2, title_text_position[1]))
        screen.blit(title_text_border, (title_text_position[0] + 2, title_text_position[1]))
        screen.blit(title_text_border, (title_text_position[0], title_text_position[1] - 2))
        screen.blit(title_text_border, (title_text_position[0], title_text_position[1] + 2))
        screen.blit(title_text, title_text_position)

        screen.blit(start_button_border, (settings.WIDTH // 2 - start_button.get_width() // 2 - 2, settings.HEIGHT // 2 + 50))
        screen.blit(start_button_border, (settings.WIDTH // 2 - start_button.get_width() // 2 + 2, settings.HEIGHT // 2 + 50))
        screen.blit(start_button_border, (settings.WIDTH // 2 - start_button.get_width() // 2, settings.HEIGHT // 2 + 50 - 2))
        screen.blit(start_button_border, (settings.WIDTH // 2 - start_button.get_width() // 2, settings.HEIGHT // 2 + 50 + 2))
        screen.blit(start_button, (settings.WIDTH // 2 - start_button.get_width() // 2, settings.HEIGHT // 2 + 50))

        screen.blit(exit_button_border, (settings.WIDTH // 2 - exit_button.get_width() // 2 - 2, settings.HEIGHT // 2 + 100))
        screen.blit(exit_button_border, (settings.WIDTH // 2 - exit_button.get_width() // 2 + 2, settings.HEIGHT // 2 + 100))
        screen.blit(exit_button_border, (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT // 2 + 100 - 2))
        screen.blit(exit_button_border, (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT // 2 + 100 + 2))
        screen.blit(exit_button, (settings.WIDTH // 2 - exit_button.get_width() // 2, settings.HEIGHT // 2 + 100))

        screen.blit(checkbox_label_border, (checkbox_rect.left - checkbox_label.get_width() - 10 - 2, checkbox_rect.top))
        screen.blit(checkbox_label_border, (checkbox_rect.left - checkbox_label.get_width() - 10 + 2, checkbox_rect.top))
        screen.blit(checkbox_label_border, (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top - 2))
        screen.blit(checkbox_label_border, (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top + 2))
        screen.blit(checkbox_label, (checkbox_rect.left - checkbox_label.get_width() - 10, checkbox_rect.top))
        screen.blit(checkbox, checkbox_rect)

        return title_text, start_button, exit_button, checkbox, checkbox_rect

def game_state_game():
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.WIDTH, settings.GRID_SIZE * 2))
        pygame.draw.rect(screen, settings.GREY, (0, settings.HEIGHT - settings.GRID_SIZE, settings.WIDTH, settings.GRID_SIZE))
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.GRID_SIZE, settings.HEIGHT))
        pygame.draw.rect(screen, settings.GREY, (settings.WIDTH - settings.GRID_SIZE, 0, settings.GRID_SIZE, settings.HEIGHT))
