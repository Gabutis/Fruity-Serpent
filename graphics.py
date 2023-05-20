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