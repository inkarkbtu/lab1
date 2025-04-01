import sys
import pygame 
pygame.init()
size=width,height=800,600
screen=pygame.display.set_mode(size)
pygame.display.set_caption("ball game")
clock = pygame.time.Clock()

white=(255,255,255)
red=(255,0,0)
x,y=width//2,height//2

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    pygame.draw.circle(screen,red,(x,y),25)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x-25>0:
        x-=20
    if keys[pygame.K_RIGHT] and x+25<width:
        x+=20
    if keys[pygame.K_UP] and y-25>0:
        y-=20
    if keys[pygame.K_DOWN] and y+25<height:
        y+=20
    
    pygame.display.update()

