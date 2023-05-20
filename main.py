import pygame
import sys
import settings
import klases
import graphics
import tkinter as tk
from tkinter import messagebox


def play_game():
    menu_window.destroy()
    window.quit()
    game_window = tk.Toplevel(window)
    game_window.title("Snake Game")
    pygame.init()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption('Baigiamasis Gyvatukas')

    snake = klases.Snake()
    food = klases.Food(snake)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_s and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_a and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_d and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        snake.move()

        if snake.check_collision():
            pygame.quit()
            sys.exit()

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.generate_position(snake)

        screen.blit(graphics.background, (0, 0))
        snake.draw(screen)
        food.draw(screen)
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.WIDTH, settings.GRID_SIZE * 2))
        pygame.draw.rect(screen, settings.GREY, (0, settings.HEIGHT - settings.GRID_SIZE, settings.WIDTH, settings.GRID_SIZE))
        pygame.draw.rect(screen, settings.GREY, (0, 0, settings.GRID_SIZE, settings.HEIGHT))
        pygame.draw.rect(screen, settings.GREY, (settings.WIDTH - settings.GRID_SIZE, 0, settings.GRID_SIZE, settings.HEIGHT))
        pygame.display.flip()
        clock.tick(10)

def show_leaderboard():
    # Add leaderboard logic here
    print("Leaderboard")
    messagebox.showinfo("Leaderboard", "Showing the leaderboard!")

def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("Snake Game Menu")

    # Create the menu window
    menu_window = tk.Frame(window)
    menu_window.pack(padx=300, pady=300)

    # Create the menu buttons
    play_button = tk.Button(menu_window, text="Play", width=15, command=play_game)
    play_button.pack()

    leaderboard_button = tk.Button(menu_window, text="Leaderboard", width=15, command=show_leaderboard)
    leaderboard_button.pack(pady=10)

    exit_button = tk.Button(menu_window, text="Exit", width=15, command=exit_game)
    exit_button.pack()

    # Start the Tkinter event loop
    window.mainloop()