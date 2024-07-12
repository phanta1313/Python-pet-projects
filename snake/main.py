import pygame
import sys
import random

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = clock.tick(60) / 1000
circle_radius = 40
circle_pos = pygame.Vector2(width/2,height/2)

score = 0

def place_food(count: int) -> list:
    food_positions = []
    for i in range(count):
        random_pos = pygame.Vector2(random.randint(0, width - 20), random.randint(0, height - 20))
        food_positions.append(random_pos)
    return food_positions
    
def move(pos: pygame.Vector2, speed:int) -> None:
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        pos.y -= speed * dt
    if keys[pygame.K_s]:
        pos.y += speed * dt
    if keys[pygame.K_a]:
        pos.x -= speed * dt
    if keys[pygame.K_d]:
        pos.x += speed * dt


food_positions = place_food(10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    for pos in food_positions:
        pygame.draw.circle(screen, "red", (int(pos.x), int(pos.y)), 20)

    pygame.draw.circle(screen, "white", circle_pos, circle_radius)

    move(circle_pos, 5)

    for food_pos in food_positions[:]:
        if circle_pos.distance_to(food_pos) < circle_radius + 20:
            food_positions.remove(food_pos)
            score += 1

    pygame.display.flip()
    

pygame.quit()
sys.exit()

