import pygame
import datetime

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mickeyclock!")
pygame.display.set_icon(pygame.image.load("lab7/images/mickeyclock.png"))
white = 255, 255, 255
clock = pygame.image.load("lab7/images/main-clock.png")
clockmickey = pygame.transform.scale(clock, (600, 600))
mickey_rect = clockmickey.get_rect()
left_arm = pygame.image.load("lab7/images/left-hand.png")
right_arm = pygame.image.load("lab7/images/right-hand.png")

def rotating(image, angle):
    return pygame.transform.rotate(image, angle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(white)
    x = (width - mickey_rect.width)//2
    y = (height - mickey_rect.height)//2
    screen.blit(clockmickey, (x, y))

    current_time = datetime.datetime.now()
    sec = current_time.second
    min = current_time.minute

    sec_angle = -sec * 6
    min_angle = -(min * 6 + sec * 0.1)

    rot_leftarm = rotating(left_arm, sec_angle)
    rot_rightarm = rotating(right_arm, min_angle)
    leftarm_rect = rot_leftarm.get_rect(center=(x+300, y+300))
    rightarm_rect = rot_rightarm.get_rect(center=(x+300, y+300))

    screen.blit(rot_leftarm, leftarm_rect)
    screen.blit(rot_rightarm, rightarm_rect)
    
    pygame.time.delay(1000)
    pygame.display.update()
