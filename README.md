# Cubic Odyssey

This is my project for Hack Club, enjoy!

## Overview

Welcome to **Cubic Odyssey**, a maze-solving game built with **Pygame**! In this game, you navigate through various levels, avoiding walls and trying to reach the finish point. The game provides an easy way to create your own levels by editing simple `.txt` files.

## How to Create Your Own Level

To create your own level, follow these steps:

1. Create a `.txt` file.
2. Define your level using the following symbols:
    - `W` represents walls.
    - `.` represents walkable spaces.
    - `P` is the starting point of the player.
    - `F` is the finish point (the goal).
   
Here is an example of a basic level layout:

```
WWWWWWWWWWWWWWWWWWWWW
W..................FW
W.W.W.W.W.W.W.W.W.W.W
W...................W
W.W.W.W.W.W.W.W.W.W.W
W.P.................W
WWWWWWWWWWWWWWWWWWWWW
```

### Symbol Explanation:
- `W`: Wall (impassable)
- `.`: Walkable space (the player can move here)
- `P`: Player's starting position
- `F`: Finish (goal)

Each level consists of rows of characters. You can use any text editor to create the `.txt` file, ensuring the walls and paths are laid out correctly.

### Tips:
- Make sure there is only one `P` (player start) and one `F` (finish) in each level.
- You can customize the size of the grid by adjusting the number of characters per row and the number of rows.
- Use `W` to create boundaries and obstacles for the player.

## File Locations

Place your level files in the `Mazes` directory within the project folder. The game will automatically load levels from this directory.

### Example Level Files:
- `level1.txt`
- `level2.txt`
- `level3.txt`

Simply add more `.txt` files to this folder to create additional levels or use the **level-generator.py** file it will automatically make a 21 by 21 level in the right Folder with the right number

## How to Play

1. Start the game.
2. Use the arrow keys (or `W`, `A`, `S`, `D`) to move the player.
3. Reach the finish point (`F`) to complete the level.
4. Once you reach the finish, the game will load the next level, if available.

## Contributions

Feel free to modify the code and levels. Contributions to the project are welcome!

## License

This project is open-source and free to use.