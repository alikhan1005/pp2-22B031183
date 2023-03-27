import pygame
pygame.init()

width = 600
height = 400

ball_radius = 25
ball_diameter = ball_radius * 2
pos_x = (width - ball_diameter) // 2
pos_y = (height - ball_diameter)/ 2

move = 20

white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ball move")

clock = pygame.time.Clock()

def draw_ball():
    pygame.draw.circle(screen, red, (pos_x, pos_y), ball_radius)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if pos_y - move >= ball_radius:
                    pos_y -= move
            elif event.key == pygame.K_DOWN:
                if pos_y + move <= height - ball_radius:
                    pos_y += move
            elif event.key == pygame.K_LEFT:
                if pos_x - move >= ball_radius:
                    pos_x -= move
            elif event.key == pygame.K_RIGHT:
                if pos_x + move <= width - ball_radius:
                    pos_x += move

    screen.fill(white)

    draw_ball()

    pygame.display.update()

    clock.tick(60)