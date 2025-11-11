import pygame
import random

# Game constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

def generate_food(snake_body):
    while True:
        food_x = random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE
        food_y = random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE
        food_pos = (food_x, food_y)
        if food_pos not in snake_body:  # Ensure food doesn't spawn on snake
            return food_pos

def game_over_screen(score):
    font = pygame.font.SysFont("arial", 40)
    game_over_text = font.render("Game Over!", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000) # Wait 3 seconds before closing

def main():
    snake_body = [(WIDTH // 2, HEIGHT // 2)]
    snake_direction = "RIGHT"
    food_pos = generate_food(snake_body)
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Move the snake
        head_x, head_y = snake_body[0]
        if snake_direction == "UP":
            head_y -= GRID_SIZE
        elif snake_direction == "DOWN":
            head_y += GRID_SIZE
        elif snake_direction == "LEFT":
            head_x -= GRID_SIZE
        elif snake_direction == "RIGHT":
            head_x += GRID_SIZE

        new_head = (head_x, head_y)

        # Game over conditions
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake_body):
            game_over = True

        snake_body.insert(0, new_head)

        # Check for food collision
        if new_head == food_pos:
            score += 1
            food_pos = generate_food(snake_body)
        else:
            snake_body.pop()

        screen.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_pos)
        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    game_over_screen(score)
    pygame.quit()

if __name__ == "__main__":
    main()