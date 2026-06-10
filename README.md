# Bouncing Ball Screensaver

A simple Python screensaver using Pygame that displays a red ball bouncing around a black screen.

## Description

This project creates a classic screensaver effect with a small red ball continuously bouncing off the walls of the window. The ball moves smoothly across the screen and reverses direction when it hits any edge, creating an infinite bouncing animation.

## Features

- 🔴 **Red Ball**: A small red circle that bounces across the screen
- ⬛ **Black Background**: Clean, minimalist black background
- 📐 **800x600 Window**: Default screen resolution
- ⚡ **Smooth Animation**: 60 FPS for smooth, flicker-free movement
- ⌨️ **Easy Exit**: Press **Q** to quit or close the window

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install pygame
```

## Usage

Run the script from the command line:

```bash
python ball_game.py
```

The ball will start bouncing in the center of the screen. 

### Controls

- **Q key**: Quit the program
- **Close window**: Also exits the program

## How It Works

The script uses Pygame to:
- Create a window with a black background
- Draw a red circle (the ball)
- Update the ball's position based on velocity vectors
- Detect collisions with screen edges and reverse the ball's direction
- Run at a constant frame rate for smooth animation

## File Structure

```
ball_game.py - Main script containing the screensaver logic
README.md    - This file
```

## License

Feel free to use and modify this project as needed.
