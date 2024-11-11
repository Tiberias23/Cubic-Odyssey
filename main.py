import pygame
import sys

# Pygame initialisieren
pygame.init()

# Bildschirm erstellen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bewegung eines Objekts")

# Farben für Light- und Dark-Mode
light_mode_colors = {
    "background": (255, 255, 255),  # Weiß
    "text": (0, 0, 0),              # Schwarz
    "object": (0, 0, 255)           # Blau
}

dark_mode_colors = {
    "background": (30, 30, 30),     # Dunkelgrau
    "text": (255, 255, 255),        # Weiß
    "object": (0, 255, 0)           # Grün
}

current_mode = "dark"
colors = dark_mode_colors  # Aktuelles Farbschema ist Light-Mode

# Schriftart für Text
font = pygame.font.SysFont(None, 48)

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
    # Mit der Taste "L" oder "D" zwischen den Modi wechseln
    if keys[pygame.K_l]:
        current_mode = "light"
        colors = light_mode_colors
    if keys[pygame.K_d]:
        current_mode = "dark"
        colors = dark_mode_colors
    # Bildschirm füllen (Hintergrund)
    screen.fill(colors["background"])

    # Text anzeigen, um den aktuellen Modus zu zeigen
    mode_text = font.render(f"Try to solv This Maze", True, colors["text"])
    screen.blit(mode_text, (35, 35))

    # Ein Objekt in der Farbe des aktuellen Modus zeichnen
    pygame.draw.rect(screen, colors["object"], (player_x, player_y, 25, 25))

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(30)
