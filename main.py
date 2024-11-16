import pygame
import sys
import os
import re  # Zum Extrahieren der Zahlen aus den Dateinamen

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
    "wand": (176, 174, 153),
    "finish": (255, 0, 0),  # Rot für das Ziel
}

light_mode_colors = {
    "background": (255, 255, 255),  # Weiß
    "text": (0, 0, 0),  # Schwarz
    "object": (0, 255, 0),  # Grün
    "wand": (120, 120, 120),
    "finish": (255, 0, 0),  # Rot für das Ziel
}

# Aktuelles Farbschema ist Dark-Mode
colors = dark_mode_colors

# Spielerklasse
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(colors["object"])  # Grün für Spieler
        self.rect = self.image.get_rect(center=(x, y))
        self.normal_speed = 5
        self.fast_speed = 10

    def update_color(self):
        self.image.fill(colors["object"])  # Aktualisiert die Farbe des Spielers

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

    def update_color(self):
        self.image.fill(colors["wand"])  # Aktualisiert die Farbe der Wand


# Finish-Klasse (Ziel)
class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colors["finish"])  # Rote Farbe für das Ziel
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_color(self):
        self.image.fill(colors["finish"])  # Aktualisiert die Farbe des Ziels


# Funktion, um Level-Layout aus einer Datei zu laden
def load_level(file_name):
    with open(file_name, 'r') as f:
        layout = f.read().splitlines()
    return layout


# Funktion, um Wände und das Ziel basierend auf dem Level-Layout zu erstellen
def create_level(layout):
    wall_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()
    tile_size = 40  # Größe jeder "Kachel"
    player_position = (100, 100)  # Default-Position für den Spieler

    for y, row in enumerate(layout):
        for x, col in enumerate(row):
            if col == "W":
                wall = Wall(x * tile_size, y * tile_size, tile_size, tile_size)
                wall_group.add(wall)
            elif col == "P":
                player_position = (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2)
            elif col == "F":
                finish = Finish(x * tile_size, y * tile_size, tile_size, tile_size)
                finish_group.add(finish)

    return wall_group, player_position, finish_group


# Funktion zum Umschalten des Farbmodus und Aktualisieren der Sprite-Farben
def toggle_mode(mode):
    global colors
    if mode == "dark":
        colors = dark_mode_colors
    else:
        colors = light_mode_colors

    # Aktualisiert die Farben von Player, Wänden und Ziel
    player.update_color()
    for wall in walls:
        wall.update_color()
    for finish in finish_group:
        finish.update_color()


# Funktion zum Laden von Level-Dateien aus dem Ordner
def load_level_files_from_directory(directory_path):
    # Alle .txt-Dateien im angegebenen Ordner suchen
    level_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]
    level_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    return [os.path.join(directory_path, file) for file in level_files]


# Funktion, um das nächste Level zu laden
def load_next_level(level_index, level_files):
    if level_index < len(level_files):
        return load_level(level_files[level_index]), level_files[level_index]
    else:
        return None, None  # Keine weiteren Level


# Hauptschleife
clock = pygame.time.Clock()
current_mode = "dark"  # Aktueller Modus

# Ordner mit den Level-Dateien
level_folder = "Mazes"  # Beispiel-Pfad

# Lade alle Level-Dateien aus dem Ordner
level_files = load_level_files_from_directory(level_folder)

# Startlevel laden
current_level_index = 0
level_layout, level_name = load_next_level(current_level_index, level_files)
level_name_without_extension = os.path.splitext(os.path.basename(level_name))[0]
walls, player_start_pos, finish_group = create_level(level_layout)

# Spieler an der definierten Startposition erstellen
player = Player(*player_start_pos)
player_group = pygame.sprite.GroupSingle(player)

# Schriftart für Text
font = pygame.font.SysFont(None, 48)

while True:
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Farbmodus umschalten
    if keys[pygame.K_1]:
        current_mode = "dark"
        toggle_mode(current_mode)
    elif keys[pygame.K_2]:
        current_mode = "light"
        toggle_mode(current_mode)

    # Spieler-Update mit Kollisionsprüfung
    player.update(walls)
    # Überprüfen, ob der Spieler das Ziel erreicht hat
    if pygame.sprite.spritecollideany(player, finish_group):
        print("Ziel erreicht!")  # Debug: Zeigt an, wenn das Ziel erreicht wurde
        current_level_index += 1  # Nächstes Level laden

        # Neues Level laden
        level_layout, level_name = load_next_level(current_level_index, level_files)

        if level_layout:  # Wenn ein neues Level existiert
            walls, player_start_pos, finish_group = create_level(level_layout)
            player.rect.center = player_start_pos  # Spieler an die neue Startposition setzen
            # Update den Levelnamen ohne Dateiendung
            level_name_without_extension = os.path.splitext(os.path.basename(level_name))[0]
        else:
            print("You have reached the last level")
            mode_text = font.render(
                "You have reached the last level. Create more levels yourself!", True, colors["text"]
            )
            screen.fill(colors["background"])
            screen.blit(mode_text, (0, 400))
            pygame.display.flip()
            pygame.time.wait(4000)  # Warte 4 Sekunden, bevor das Spiel beendet wird
            pygame.quit()
            sys.exit()

    # Bildschirm zeichnen
    screen.fill(colors["background"])
    walls.draw(screen)
    player_group.draw(screen)
    finish_group.draw(screen)

    # Levelnamen anzeigen
    level_name_text = font.render(f"Level: {level_name_without_extension}", True, colors["text"])
    screen.blit(level_name_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
