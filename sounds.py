import pygame
import os


base_path = r'C:\Users\vidma\PycharmProjects\Fruity_Serpent'

sound_bite_path = os.path.join(base_path, "sounds", "bite.mp3")
sound_bite = pygame.mixer.Sound(sound_bite_path)
sound_bite.set_volume(0.4)

sound_collision_path = os.path.join(base_path, "sounds", "collision.mp3")
sound_collision = pygame.mixer.Sound(sound_collision_path)
sound_collision.set_volume(0.4)

background_sound_path = os.path.join(base_path, "sounds", "background_sound.mp3")
pygame.mixer.music.load(background_sound_path)
pygame.mixer.music.set_volume(0.05)