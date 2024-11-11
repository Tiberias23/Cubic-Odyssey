import pygame
import sys

# Pygame initialisieren
pygame.init()
# Bildschirm erstellen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cubic Odyssey")
# Farben für Light- und Dark-Mode
light_mode_colors = {
    "background": (255, 255, 255),  # Weiß
    "text": (0, 0, 0),  # Schwarz
    "object": (0, 0, 255),  # Blau
    "wand": (0, 0, 0)  # Schwarz
}

dark_mode_colors = {
    "background": (30, 30, 30),  # Dunkelgrau
    "text": (255, 255, 255),  # Weiß
    "object": (0, 255, 0),  # Grün
    "wand": (255, 255, 255)  # Weiß
}

current_mode = "dark"
colors = dark_mode_colors  # Aktuelles Farbschema ist Light-Mode


# Plyer class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))  # Grün für Spieler
        self.rect = self.image.get_rect(center=(100, 100))
        self.speed = 5

    def update(self, wall):
        # Position vor der Bewegung speichern
        old_rect = self.rect.copy()

        # Tasten abfragen
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += self.speed

        # Kollisionsprüfung mit den Wänden
        if pygame.sprite.spritecollideany(self, wall):
            # Zur vorherigen Position zurücksetzen, wenn eine Wand getroffen wird
            self.rect = old_rect


# Wandklasse
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colors["object"])  # Rot für Wände
        self.rect = self.image.get_rect(topleft=(x, y))


# Schriftart für Text
font = pygame.font.SysFont(None, 48)

# Gruppen erstellen
player = Player()
player_group = pygame.sprite.GroupSingle(player)

walls = pygame.sprite.Group()
walls.add(Wall(100, 100, 15, 420))  # Wand Links
walls.add(Wall(540, 100, 15, 420))  # Wand Rechts
walls.add(Wall(115, 100, 425, 15))  # Wand Oben
walls.add(Wall(115, 505, 425, 15))  # Wand Unten

keys = pygame.key.get_pressed()
# Hauptschleife
clock = pygame.time.Clock()
while True:
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if keys[pygame.K_l]:
        current_mode = "light"
    if keys[pygame.K_d]:
        current_mode = "dark"
    # Spieler-Update mit Kollisionsprüfung
    player.update(walls)

    # Mit der Taste "L" oder "D" zwischen den Modi wechseln
    keys = pygame.key.get_pressed()

    # Bildschirm zeichnen
    screen.fill((30, 30, 30))
    walls.draw(screen)
    player_group.draw(screen)

    # Text anzeigen, um den aktuellen Modus zu zeigen
    mode_text = font.render(f"Try to solv This Maze", True, colors["text"])
    screen.blit(mode_text, (35, 35))

    pygame.display.flip()
    clock.tick(60)
