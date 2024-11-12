import pygame
import sys

# Pygame initialisieren
pygame.init()
# Bildschirm erstellen
screen = pygame.display.set_mode((1000, 900))

pygame.display.set_caption("Cubic Odyssey")

# Farben für Light- und Dark-Mode
dark_mode_colors = {
    "background": (30, 30, 30),  # Dunkelgrau
    "text": (255, 255, 255),  # Weiß
    "object": (0, 255, 0),  # Grün
    "wand": (176, 174, 153)
}

current_mode = "dark"
colors = dark_mode_colors  # Aktuelles Farbschema ist dark-Mode


# Spielerklasse
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(colors["object"])  # Grün für Spieler
        self.rect = self.image.get_rect(center=(x, y))
        self.normal_speed = 5
        self.fast_speed = 30

    def move_with_collision(self, dx, dy, walls):
        """Bewegt den Spieler in kleinen Schritten und prüft nach jedem Schritt auf Kollision."""
        step = 1 if abs(dx) <= 1 and abs(dy) <= 1 else 2  # Schrittgröße
        while dx != 0 or dy != 0:
            # Schrittweise pro Richtung bewegen
            if abs(dx) >= step:
                self.rect.x += step * (1 if dx > 0 else -1)
                dx -= step * (1 if dx > 0 else -1)
            else:
                self.rect.x += dx
                dx = 0

            if pygame.sprite.spritecollideany(self, walls):
                self.rect.x -= step * (1 if dx > 0 else -1)
                break

            if abs(dy) >= step:
                self.rect.y += step * (1 if dy > 0 else -1)
                dy -= step * (1 if dy > 0 else -1)
            else:
                self.rect.y += dy
                dy = 0

            if pygame.sprite.spritecollideany(self, walls):
                self.rect.y -= step * (1 if dy > 0 else -1)
                break

    def update(self, wall_group):
        # Tastenabfragen
        keys = pygame.key.get_pressed()

        # Geschwindigkeit festlegen: Schnell, wenn Shift gedrückt ist
        speed = self.fast_speed if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else self.normal_speed

        # Bewegung in jede Richtung berechnen
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += speed

        # Schrittweise bewegen und Kollision prüfen
        self.move_with_collision(dx, dy, wall_group)


# Wandklasse
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colors["wand"])  # Farbe der Wand
        self.rect = self.image.get_rect(topleft=(x, y))


# Funktion, um Level-Layout aus einer Datei zu laden
def load_level(file_name):
    with open(file_name, 'r') as f:
        layout = f.read().splitlines()
    return layout


# Funktion, um Wände basierend auf dem Level-Layout zu erstellen
def create_level(layout):
    wall_group = pygame.sprite.Group()
    tile_size = 40  # Größe jeder "Kachel"
    player_position = (100, 100)  # Default-Position für den Spieler

    for y, row in enumerate(layout):
        for x, col in enumerate(row):
            if col == "W":  # W steht für Wand
                wall = Wall(x * tile_size, y * tile_size, tile_size, tile_size)
                wall_group.add(wall)
            elif col == "P":  # P steht für Spieler-Startposition
                player_position = (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2)

    return wall_group, player_position


# Level aus Datei laden und Wände erstellen
level_layout = load_level("C:\\Users\\tiber\\PycharmProjects\\Cubic-Odyssey\\Mazes\\level.txt")

walls, player_start_pos = create_level(level_layout)

# Spieler an der definierten Startposition erstellen
player = Player(*player_start_pos)
player_group = pygame.sprite.GroupSingle(player)

# Schriftart für Text
font = pygame.font.SysFont(None, 48)

# Hauptschleife
clock = pygame.time.Clock()
while True:
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Spieler-Update mit Kollisionsprüfung
    player.update(walls)

    # Bildschirm zeichnen
    screen.fill(colors["background"])
    walls.draw(screen)
    player_group.draw(screen)

    # Text anzeigen, um den aktuellen Modus zu zeigen
    mode_text = font.render(f"Try to solve This Maze", True, colors["text"])
    screen.blit(mode_text, (440, 30))

    pygame.display.flip()
    clock.tick(60)
