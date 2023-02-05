import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
width = 500
height = 500

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the clock for controlling the game speed
clock = pygame.time.Clock()

# Set the font for displaying the score
font = pygame.font.Font(None, 30)

# Define the size of each block in the game
block_size = 10

# Initialize the score
score = 0

# Define the initial position and size of the snake
x = 250
y = 250
snake_size = 10
snake_list = []
snake_length = 1

# Define the initial position of the food
food_x = 0
food_y = 0

# Function for generating the food
def generate_food():
    global food_x, food_y
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

# Generate the first food
generate_food()

# Set the initial direction of the snake
direction = "right"

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle the key events for controlling the snake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = "left"
        if keys[pygame.K_RIGHT]:
            direction = "right"
        if keys[pygame.K_UP]:
            direction = "up"
        if keys[pygame.K_DOWN]:
            direction = "down"

    # Move the snake in the desired direction
    if direction == "right":
        x += block_size
    if direction == "left":
        x -= block_size
    if direction == "up":
        y -= block_size
    if direction == "down":
        y += block_size

    # Check if the snake has collided with the walls
    if x >= width or x < 0 or y >= height or y < 0:
        running = False

    # Add the new position of the snake to the snake_list
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    # Check if the length of the snake_list is more than the snake_length
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check if the snake has collided with itself
    for block in snake_list[:-1]:
