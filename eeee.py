import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((640, 480))

# Set caption
pygame.display.set_caption("My first game screen")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    screen.fill(white)

    # Rectangle in center
    pygame.draw.rect(screen, blue, (220, 190, 200, 100))

    pygame.display.update()

pygame.quit()