import pygame

pygame.init()

screen_width = 500
screen_height = 500
ball_radius = 25
ball_diameter = ball_radius * 2
pos_x = (screen_width ) / 2
pos_y = (screen_height ) / 2
move = 20
dx, dy = 0, 0

screen = pygame.display.set_mode((screen_width, screen_height))
# screen.fill((255,255,255))
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()

while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type  == pygame.KEYDOWN:
            # event.type  = pygame.key.get_event.type ()
            if event.key == pygame.K_UP:
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1
            elif event.key ==pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key ==pygame.K_RIGHT:
                dx = 1
                dy = 0
            else:
                dx = 0
                dy = 0
        pos_x += dx*move
        pos_y += dy*move

    screen.fill((255,255,255))
    pygame.draw.circle(screen, 
    (255, 0, 0), 
    (pos_x, pos_y), 
    ball_radius)
   
    pygame.display.flip()
    clock.tick(60)