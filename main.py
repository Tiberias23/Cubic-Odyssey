import pygame
import sys

background = input("Light or Dark-mode").lower()
# Pygame initialisieren
pygame.init()
background_color = (0, 0, 0)
# Bildschirm erstellen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bewegung eines Objekts")

if background == "light" or 1:
    background_color = (255, 255, 255)
if background == "dark" or 2:
    background_color = (0, 0, 0)

rot = (255, 0, 0)
# Startposition des Objekts
player_x, player_y = 400, 300
speed = 5  # Geschwindigkeit des Objekts

# Hauptschleife
clock = pygame.time.Clock()
while True:
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tastenstatus abfragen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:  # Nach oben
        player_y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Nach unten
        player_y += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Nach links
        player_x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Nach rechts
        player_x += speed

    # Bildschirm füllen (Hintergrund)
    screen.fill(background_color)

    # Objekt zeichnen
    pygame.draw.rect(screen, rot, (player_x, player_y, 50, 50))  # Ein rotes Quadrat

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Frame-Rate begrenzen
    clock.tick(60)  # 60 FPS
