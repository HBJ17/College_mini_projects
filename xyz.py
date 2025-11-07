import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("My Game")
icon = pygame.image.load("D:\Studies\Projects\Python\College_files\Images\console.png")
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((255,255,255))
        pygame.display.update()
        