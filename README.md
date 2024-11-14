# Cubic Odyssey

**Cubic Odyssey** is a 2D maze-solving game built with Python and Pygame. Navigate through challenging levels filled with obstacles, walls, and narrow corridors, and find your way out of the maze! The game features a dynamic Light and Dark Mode, adding a unique visual experience while playing. With a sprint mechanic, players can move faster through the maze when holding the Shift key—just be careful not to run into walls!

## Features

- **Dynamic Light and Dark Mode**: Switches between light and dark color schemes for a better gaming experience.
- **Sprint Mechanic**: Hold Shift to move faster through the maze.
- **Collision Detection**: Prevents the player from moving through walls.
- **Level Design with `.txt` Files**: Levels are stored in `.txt` files, making it easy to create and edit levels without modifying the game code.
- **Simple Level Management**: Define walls, open spaces, and starting points in a text file with symbols, making level creation accessible for everyone.

## How to Play

1. **Move**: Use the arrow keys or WASD to navigate through the maze.
2. **Sprint**: Hold Shift (Left or Right) to move faster.
3. **Objective**: Find your way through the maze without hitting the walls.
4. **Change the Theme**: Use `1` for Darkmode and `2` for Lightmode

## Getting Started

### Prerequisites

- Python 3.x
- Pygame (`pip install pygame`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cubic-odyssey.git
   ```

2. Navigate to the project folder:

   ```bash
   cd cubic-odyssey
   ```

3. Install dependencies:

   ```bash
   pip install pygame
   ```

4. Run the game:

   ```bash
   python main.py
   ```

### Level Editing

Levels are stored in `.txt` files, where:
- `W` represents walls
- `.` represents empty spaces
- `P` represents the player starting point

For example, here’s a sample level file structure:

```
WWWWWWWWWW
W........W
W.W.W.W.WW
W........W
W.W.W.W.WW
W.P......W
WWWWWWWWWW
```

You can create custom levels by modifying or adding new `.txt` files with similar structures.
