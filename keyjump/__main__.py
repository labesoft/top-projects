"""The Keyboad Jump Game Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Keyboad Jump Game Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing modules
import random

import pygame


def new_word(a_speed):
    xcor = random.randint(300, 700)
    ycor = 200  # y-cor
    a_speed += 0.1
    a_word = ''
    words = open("words.txt").read().split(', ')
    next_word = random.choice(words)
    return next_word, a_word, xcor, ycor, a_speed


def draw_text(display, text, size, x, y):
    game_font = pygame.font.Font(font_name, size)
    text_surface = game_font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)


def game_front_screen(go, gs):
    gameDisplay.blit(background, (0, 0))
    if not go:
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 8)
        draw_text(gameDisplay, "Score : " + str(score), 70, WIDTH / 2,
                  HEIGHT / 4)
        draw_text(gameDisplay, "Press Space bar to restart", 50, WIDTH / 2,
                  HEIGHT / 2)
        gs = True
        go = True
    else:
        draw_text(gameDisplay, "Press any key to begin!", 54, WIDTH / 2, 500)
        gs = False
        go = False
    pygame.display.flip()
    waiting = True
    while waiting:
        for an_event in pygame.event.get():
            if an_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if an_event.type == pygame.KEYUP and an_event.key == pygame.K_SPACE:
                waiting = False
    return go, gs


if __name__ == '__main__':
    """Main entry point of keyjump"""
    # Initialize window
    font_name = pygame.font.match_font('comic.ttf')
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    black = (0, 0, 0)

    # Define functions
    # Main loop
    game_over = True
    game_start = True
    while True:
        if game_over:
            if game_start:
                word_speed = 0.5
                score = 0
                displayword, yourword, x_cor, y_cor, word_speed = new_word(
                    word_speed)
                pygame.init()
                gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
                background = pygame.image.load('keyback.jpg')
                # scale image
                background = pygame.transform.scale(background, (WIDTH, HEIGHT))
                font = pygame.font.Font('comic.ttf', 40)
                game_over, game_start = game_front_screen(game_over, game_start)
            game_start = False
        else:
            if y_cor < HEIGHT - 5:
                pygame.display.update()
            else:
                game_over, game_start = game_front_screen(game_over, game_start)
        game_over = False
        background = pygame.image.load('teacher-background.jpg')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        character = pygame.image.load('char.jpg')
        character = pygame.transform.scale(character, (50, 50))
        wood = pygame.image.load('wood-.png')
        wood = pygame.transform.scale(wood, (90, 50))
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(wood, (x_cor - 50, y_cor + 15))
        gameDisplay.blit(character, (x_cor - 100, y_cor))
        draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
        draw_text(gameDisplay, 'Score:' + str(score), 40, WIDTH / 2, 5)
        y_cor += word_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                yourword += pygame.key.name(event.key)
                if displayword.startswith(yourword):
                    if displayword == yourword:
                        score += len(displayword)
                        (displayword, yourword,
                         x_cor, y_cor, word_speed) = new_word(word_speed)
                else:
                    game_over, game_start = game_front_screen(game_over,
                                                              game_start)
