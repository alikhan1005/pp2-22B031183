import pygame
import datetime
import time
pygame.init()

width = 900
height = 700
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Mickey Mouse Clock")

mickey_body = pygame.image.load("/Users/alikhankudaibergen/Documents/pp2/tsis7/images/main-clock.png")
left = pygame.image.load("/Users/alikhankudaibergen/Documents/pp2/tsis7/images/left-hand.png")
right = pygame.image.load("/Users/alikhankudaibergen/Documents/pp2/tsis7/images/right-hand.png")

minute_angle = 0
second_angle = 0

font = pygame.font.SysFont(None, 60)

def draw_clock(screen):

    body_rect = mickey_body.get_rect(center=(width/2, height/2))
    screen.blit(mickey_body, body_rect)
       # Rotate Mickey's hands according to current time
    current_time = datetime.datetime.now()
    minute_angle = current_time.minute * 6 - 84 # 6 degrees per minute
    second_angle = current_time.second * 6 - 88 # 6 degrees per second
    minute_hand = pygame.transform.rotate(right, -minute_angle)
    second_hand = pygame.transform.rotate(left, -second_angle)
    # rotated_image = pygame.transform.rotate(image, angle)
    minute_pos = minute_hand.get_rect(center=surface.get_rect().center)
    second_pos = second_hand.get_rect(center=surface.get_rect().center)
    # Draw Mickey's hands
    surface.fill((0, 0, 0, 0))
    screen.blit(minute_hand, minute_pos)
    screen.blit(second_hand, second_pos)
    
    digital_clock = font.render(time.strftime("%H:%M:%S"), True, (45, 10, 38))
    screen.blit(digital_clock, (width/2 - digital_clock.get_width()/2, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill((0, 0, 0))
    
    draw_clock(screen)
   
    pygame.display.flip()