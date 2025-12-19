import pygame
import sys
import random

# --- General Setup ---
pygame.init()
clock = pygame.time.Clock()

# --- Screen Setup ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# --- Colors ---
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# --- Game Rectangles (The "Actors") ---
# Rect(x, y, width, height)
# We place the ball in the middle
ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)
# Player on the right
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70, 10, 140)
# Opponent (AI) on the left
opponent = pygame.Rect(10, SCREEN_HEIGHT/2 - 70, 10, 140)

# --- Game Variables ---
# Speeds
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# --- Functions ---

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with Top and Bottom
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1 # Reverse vertical direction

    # Collision with Left and Right (Scoring)
    if ball.left <= 0:
        # Player scores
        player_score += 1
        ball_restart()
        
    if ball.right >= SCREEN_WIDTH:
        # Opponent scores
        opponent_score += 1
        ball_restart()

    # Collision with Paddles
    # We check if the ball rect overlaps with player or opponent rect
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1 # Reverse horizontal direction

def player_animation():
    player.y += player_speed
    
    # Keep player on screen (Boundary checks)
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_ai():
    # Simple AI: Move the paddle towards the ball's y position
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Keep opponent on screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y
    # Reset ball to center
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Send ball in random direction
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# --- Main Game Loop ---
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Key Press (Key Down)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        
        # Key Release (Key Up)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # 2. Game Logic
    ball_animation()
    player_animation()
    opponent_ai()

    # 3. Drawing
    # Clear screen first (important!)
    screen.fill(bg_color)
    
    # Draw Game Objects
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    # Draw Center Line
    pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # Draw Score
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470)) # Position slightly right of center

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470)) # Position slightly left of center

    # Update the window
    pygame.display.flip()
    
    # Limit the frame rate to 60 FPS
    clock.tick(60)