import pygame

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Marvel Battle Simulator")

# Load images
background = pygame.image.load("background.jpg")
spiderman = pygame.image.load("spiderman.png")

# Character position
x = 100
y = 300

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(spiderman, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    pygame.display.update()

pygame.quit()
