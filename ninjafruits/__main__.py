"""The Ninja Fruits Game Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Ninja Fruits Game Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing required modules
import os
import random

import pygame


def generate_random_fruits(a_fruit):
    results = {}
    fruit_path = "images/" + a_fruit + ".png"
    results[a_fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),
        'y': 800,
        'speed_x': random.randint(-10, 10),
        'speed_y': random.randint(-80, -60),
        'throw': False,
        't': 0,
        'hit': False,
    }
    if random.random() >= 0.75:
        results[a_fruit]['throw'] = True
    else:
        results[a_fruit]['throw'] = False
    return results


def draw_text(display, text, size, x, y, a_fname):
    a_font = pygame.font.Font(a_fname, size)
    text_surface = a_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)


def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()
        img_rect.x = int(x + 35 * i)
        img_rect.y = y
        display.blit(img, img_rect)


def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))


def show_gameover_screen(fname):
    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "FRUIT NINJA!", 64, WIDTH / 2, HEIGHT / 4, fname)
    if not game_over:
        draw_text(gameDisplay, "Score : " + str(score), 40, WIDTH / 2, 250,
                  fname)
    draw_text(gameDisplay, "Press a key to begin!", 24, WIDTH / 2, HEIGHT * 3
              / 4, fname)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for an_event in pygame.event.get():
            if an_event.type == pygame.QUIT:
                pygame.quit()
            if an_event.type == pygame.KEYUP:
                waiting = False


if __name__ == '__main__':
    """Main entry point of ninjafruits"""
    # Initialize window
    player_lives = 3
    score = 0
    fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']
    WIDTH = 800
    HEIGHT = 500
    FPS = 12
    pygame.init()
    pygame.display.set_caption('FRUIT NINJA - -labesoft')
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    gameDisplay.fill(BLACK)
    background = pygame.image.load('back.jpg')
    font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 32)
    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
    lives_icon = pygame.image.load('images/white_lives.png')

    # Define functions
    data = {}
    for fruit in fruits:
        data.update(generate_random_fruits(random.choice(fruits)))
    font_name = pygame.font.match_font('comic.ttf')

    # Game loop
    first_round = True
    game_over = True
    game_running = True
    while game_running:
        if game_over:
            if first_round:
                show_gameover_screen(font_name)
                first_round = False
            game_over = False
            player_lives = 3
            draw_lives(gameDisplay, 690, 5, player_lives,
                       'images/red_lives.png')
            score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(score_text, (0, 0))
        draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']
                value['y'] += value['speed_y']
                value['speed_y'] += (1 * value['t'])
                value['t'] += 1
                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))
                else:
                    data = generate_random_fruits(random.choice(fruits))
                current_position = pygame.mouse.get_pos()
                if not value['hit'] and value['x'] < current_position[0] < \
                        value['x'] + 60 \
                        and value['y'] < current_position[1] < value['y'] + 60:
                    if key == 'bomb':
                        player_lives -= 1
                        if player_lives == 0:
                            hide_cross_lives(690, 15)
                        elif player_lives == 1:
                            hide_cross_lives(725, 15)
                        elif player_lives == 2:
                            hide_cross_lives(760, 15)

                        if player_lives < 0:
                            show_gameover_screen(font_name)
                            game_over = True
                        half_fruit_path = "images/explosion.png"
                    else:
                        half_fruit_path = "images/" + "half_" + key + ".png"
                    value['img'] = pygame.image.load(half_fruit_path)
                    value['speed_x'] += 10
                    if key != 'bomb':
                        score += 1
                    score_text = font.render('Score : ' + str(score), True,
                                             (255, 255, 255))
                    value['hit'] = True
            else:
                data = generate_random_fruits(random.choice(fruits))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
