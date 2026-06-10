import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ball properties
BALL_RADIUS = 10
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = SCREEN_HEIGHT // 2
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball Screensaver")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Ball position and velocity
ball_x = BALL_START_X
ball_y = BALL_START_Y
velocity_x = BALL_SPEED_X
velocity_y = BALL_SPEED_Y

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    # Update ball position
    ball_x += velocity_x
    ball_y += velocity_y
    
    # Bounce off walls
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= SCREEN_WIDTH:
        velocity_x = -velocity_x
        ball_x = max(BALL_RADIUS, min(SCREEN_WIDTH - BALL_RADIUS, ball_x))
    
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
        velocity_y = -velocity_y
        ball_y = max(BALL_RADIUS, min(SCREEN_HEIGHT - BALL_RADIUS, ball_y))
    
    # Fill screen with black
    screen.fill(BLACK)
    
    # Draw the red ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), BALL_RADIUS)
    
    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
