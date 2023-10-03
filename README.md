# Pong Game
---
## Overview
This project is an implementation of the classic Pong game using Python's Turtle Graphics module. Pong is a two-player sports game that simulates table tennis. The game features two paddles, one on each side, and a ball that bounces between them. Players control the paddles to prevent the ball from passing their side of the screen.

---
## Components

### 1. `main.py`
This file contains the main game loop and logic. It initializes the game window, creates instances of the paddles and ball, and handles user input for controlling the paddles. The game loop manages the movement of the ball, detects collisions with the walls and paddles, and updates the score. Additionally, it provides a smooth gaming experience by limiting the frame rate and controlling the game speed.



### 2. `paddle.py`
The `Paddle` class defines the characteristics and behavior of the paddles. Each paddle is a rectangular shape that can move up or down. The `go_up` and `go_down` methods control the paddle's movement. The paddles' dimensions and movement speed have been carefully calibrated to provide a balanced gameplay experience.

### 3. `ball.py`
The `Ball` class represents the game ball. It moves continuously at a fixed speed and can bounce off walls and paddles. The `move`, `bounce_y`, `bounce_x`, and `reset_game` methods handle the ball's behavior. The ball's physics have been fine-tuned to ensure realistic and engaging gameplay.

### 4. `scoreboard.py`
The `Scoreboard` class manages the scoring system. It displays the current scores for each player on the screen. The `l_point` and `r_point` methods increment the scores when a player scores a point. The scoreboard also keeps track of the highest score achieved, providing an additional competitive element to the game.

---

## How to Play
1. Run `main.py` to start the game.
2. Player on the right uses the up and down arrow keys to control their paddle.
3. Player on the left uses the 'w' and 's' keys to control their paddle.
4. The game continues until one player reaches the winning score.

---
## Getting Started
To run this project, ensure you have Python installed on your system. Clone this repository to your local machine and run `main.py` using a Python interpreter. Optionally, you can create a virtual environment to manage dependencies.

---
## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. You can also open issues for bug reports or feature requests. Contributions that enhance gameplay mechanics, improve visuals, or add new features are highly encouraged.
