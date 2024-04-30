import pygame 
from datetime import datetime 

pygame.init()

screen = pygame.display.set_mode((800,800))
window_title = pygame.display.set_caption("Clock")

clock = pygame.time.Clock()


bg_surf = pygame.image.load("IMAGE/clock.png")
sec_surf = pygame.image.load("IMAGE/sec.png")
min_surf = pygame.image.load("IMAGE/min.png")
bg_rect = bg_surf.get_rect(center = (400, 400))

done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now=datetime.now().time()

    second_angle = -((now.second+1) * 6)
    minute_angle = -((now.minute+9) * 6) 

    rotated_sec = pygame.transform.rotate(sec_surf, second_angle)
    rotated_min = pygame.transform.rotate(min_surf, minute_angle)

    sec_rect = rotated_sec.get_rect(center = bg_rect.center)
    min_rect = rotated_min.get_rect(center = bg_rect.center)

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_sec, sec_rect)
    screen.blit(rotated_min, min_rect)

    pygame.display.flip()
    clock.tick(60)