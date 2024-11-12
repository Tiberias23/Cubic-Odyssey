import os

# Path to the “Mazes” folder
ordner_pfad = "C:\\Users\\tiber\\PycharmProjects\\Cubic-Odyssey\\Mazes"

# Count the existing files in the “Mazes” folder
bestehende_dateien = [f for f in os.listdir(ordner_pfad) if f.startswith("level") and f.endswith(".txt")]
anzahl_bestehende_dateien = len(bestehende_dateien)+1

# Number of new files to be created
anzahl = int(input("how many files do you need?"))  # how many files do you need

# Erstellen neuer Dateien
for i in range(anzahl):
    nummer = anzahl_bestehende_dateien + i  # Continue counting from the number of existing files
    dateiname = f"level{nummer}.txt"  # Create the file name
    dateipfad = os.path.join(ordner_pfad, dateiname)  # Path to the file in the folder
    with open(dateipfad, 'w') as file:
        file.write(f"""this is file {nummer}
WWWWWWWWWWWWWWWWWWWWW
W..................FW
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
W...................W
WP..................W
WWWWWWWWWWWWWWWWWWWWW
        """)  # Generates a standard level file
