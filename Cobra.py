import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('Img/astronaut-space-13-4k.jpg')
pygame.display.set_icon(icon)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Snake block size
block_size = 10

# FPS
fps = 30


# Game Over Function
def game_over():
    message = font_style.render("Game Over", True, RED)
    screen.blit(message, [WIDTH / 2 - message.get_width() / 2, HEIGHT / 2 - message.get_height() / 2])
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()


# Main Function
def play_game():
    # Initial position of Snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    # Initialize food
    foodx = round(random.randrange(0, WIDTH - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - block_size) / 10.0) * 10.0

    # Initialize snake
    snake_list = []
    snake_length = 1

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # Game Over conditions
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over()

        # Snake movement
        x1 += x1_change
        y1 += y1_change

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw food
        pygame.draw.rect(screen, GREEN, [foodx, foody, block_size, block_size])

        # Draw snake
        head = []
        head.append(x1)
        head.append(y1)
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x, y in snake_list[:-1]:
            if x == x1 and y == y1:
                game_over()

        our_snake = pygame.draw.rect(screen, BLACK, [x1, y1, block_size, block_size])

        # Snake and food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - block_size) / 10.0) * 10.0
            snake_length += 1

        # Display score
        score = font_style.render("Score: " + str(snake_length - 1), True, BLACK)
        screen.blit(score, [0, 0])

        # Update the screen
        pygame.display.update()

        # Set clock
        clock.tick(fps)

    # Run the game
play_game()
pygame.quit()
