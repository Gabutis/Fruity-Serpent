import pygame
import settings


class MusicSlider:
    def __init__(self, y_offset, width, height, min_value, max_value, name):
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.name = name

        # Set the initial value based on the current volume of the background music
        volume = pygame.mixer.music.get_volume() * 100
        self.value = int(volume)

        self.calculate_position(y_offset)

    def calculate_position(self, y_offset):
        x = settings.WIDTH // 2 - self.width // 2
        y = settings.HEIGHT // 2 - y_offset
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update_value(self, position):
        # Update the slider's value based on the position
        if position < self.rect.x:
            self.value = self.min_value
        elif position > self.rect.x + self.rect.width:
            self.value = self.max_value
        else:
            # Calculate the value based on the position within the slider
            range_width = self.max_value - self.min_value
            position_offset = position - self.rect.x
            percentage = position_offset / self.rect.width
            self.value = self.min_value + int(range_width * percentage)

        # Update the volume of the background music
        pygame.mixer.music.set_volume(self.value / 100.0)

    def draw(self, screen):
        # Draw the slider on the screen
        pygame.draw.rect(screen, settings.GREEN, self.rect)
        knob_x = self.rect.x + int(
            self.rect.width
            * (self.value - self.min_value)
            / (self.max_value - self.min_value)
        )
        knob_rect = pygame.Rect(knob_x - 5, self.rect.y - 5, 10, self.rect.height + 10)
        pygame.draw.rect(screen, settings.PURPLE, knob_rect)

        # Display the value on the slider
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, settings.PURPLE)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
        name_text = font.render(self.name, True, settings.PURPLE)
        name_text_rect = name_text.get_rect(
            center=(self.rect.centerx, self.rect.centery + self.rect.height)
        )
        screen.blit(name_text, name_text_rect)
        screen.blit(text, text_rect)


music_sound_volume = 0.05

sound_bite = pygame.mixer.Sound("sounds/bite.mp3")
sound_bite.set_volume(0.4)

sound_collision = pygame.mixer.Sound("sounds/collision.mp3")
sound_collision.set_volume(0.4)

pygame.mixer.music.load("sounds/background_sound.mp3")
pygame.mixer.music.set_volume(music_sound_volume)
