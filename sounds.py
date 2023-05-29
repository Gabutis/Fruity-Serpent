import pygame


sound_bite = pygame.mixer.Sound("sounds/bite.mp3")
sound_bite.set_volume(0.4)

sound_collision = pygame.mixer.Sound("sounds/collision.mp3")
sound_collision.set_volume(0.4)

pygame.mixer.music.load("sounds/background_sound.mp3")
pygame.mixer.music.set_volume(0.05)