# The Mini Battleships Game
This is a Python terminal game running in the Code Institute mock terminal on Heroku.
![amiresponsive screens for Battleship Game](https://github.com/OMandila/battleships_game/assets/71443713/b8b5a84d-9a88-45ae-bf6f-759d114d1314)

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [How to Play](#how-to-play)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Future features](#future-features)
- [Data Model](#data-model)
- [User Stories](#user-stories)
- [Design](#design)
  - [Responsive Design](#responsive-design)
  - [Color Scheme](#color-scheme)
  - [Font Choice](#font-choice)
  - [Icons](#icons)
  - [Wireframes](#wireframes)
- [Website Structure and Features](#website-structure-and-features)
- [Technologies Used](#technologies-used)
- [Testing and Validation](#testing-and-validation)
  - [Bugs](#bugs)
    - [Resolved Bugs](#resolved-bugs)
    - [Unresolved Bugs](#unresolved-bugs)
    - [Validator Testing](#validator-testing)
- [Deployment](#deployment)
  - [Local Setup](#local-setup)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgement](#acknowledgement)
  - [Code Inspiration](#code-inspiration)
  - [Media](#media)

## Introduction
The Mini Battleships Game is a strategy type guessing game designed for two players: the PLAYER (you) and the OPPONENT (computer).
![Battleships Game - Flowchart](https://github.com/OMandila/battleships_game/assets/71443713/d206eaf0-220e-429b-a4b1-27e8ca503ceb)

## Project Overview
This project simulates the classic Battleships game where players take turns to guess the locations of each other's ships on a hidden board with the aim of "capsizing" all the opponent's ships.
Each battleship occupies one square on the board, identified by column and row coordinates. A missile from the opponent "lands" on a square also identified by column and row coordinates.
The live version of my project is deployed [in Heroku](https://om-battleships-game-4b68485d0a26.herokuapp.com/)

## How to Play
Here’s how to get started with this game:

1. **Start the Game:** Click `Run Program` on the Heroku terminal: [Play the Mini Battleships Game on Heroku.](https://om-battleships-game-4b68485d0a26.herokuapp.com/) for the already deployed game. You could also run the script in your terminal or command prompt by executing `python run.py` or `python3 run.py`.
2. **Set Up Your Battleships:** You will be prompted to enter the number of battleships you wish to place on the board and their locations. Enter the row and column numbers to place each of your battleships.
3. **Taking Turns:** In this game, the player always starts by positioning the Battleships. Afterwards, the computer drops missiles on the board using a random function.
4. **Hit or Miss:** The computer tries to hit the player's ship by guessing their locations. A hit is marked with a Ⓧ symbol, and a miss with an x.
5. **Game End:** The game ends after the computer has dropped the missiles. The script calculates and displays the scores based on the number of hits and misses.

## Features
### Existing features
*Interactive Battleship Placement:* The Player can input their battleship positions at the beginning of the game.
![image](https://github.com/OMandila/battleships_game/assets/71443713/69cd0eb1-90a6-456e-bc74-5fc70b989475)

![image](https://github.com/OMandila/battleships_game/assets/71443713/e7f64545-acb2-46e1-b302-956ec1df5cb8)

![image](https://github.com/OMandila/battleships_game/assets/71443713/4c85131b-84c0-4cfe-8f96-30bf1b95661b)

*Automatic Enemy Fire:* The computer randomly selects targets, simulating enemy fire.

*Hit and Miss Feedback:* The board updates with symbols indicating hits and misses.

*Score Calculation:* At the end of each game, scores are calculated based on the number of ships sunk and remaining.
![image](https://github.com/OMandila/battleships_game/assets/71443713/5d30d992-73c8-4660-a205-c1e6a5f88d20)

*Automatic Restart:* The Player can restart the game every time by typing anything apart from 'N' at the end.
![image](https://github.com/OMandila/battleships_game/assets/71443713/3e8b59e4-0a6e-4982-913b-bade54b20a05)

### Future features
*Player vs. Player Mode:* Allowing two human players to compete against each other.
*Improved AI for Computer:* Making the computer's choice of targets smarter based on previous hits.
*Customizable Board Size:* Letting players choose different board sizes to vary the game's difficulty.
*Battleship Size:* Letting players vary the sizes of their battleships.
*Graphical User Interface (GUI):* Implementing a simple GUI for the game for those who prefer not to use the terminal.
*Leaderboards:* Adding a feature to track high scores or win/loss records over time.

## Data Model
The game uses a simple data model represented by a 2D list (list of lists) to create and manipulate the game board:

- Board Representation: The board is a 2D list where each sublist represents a row on the board. Each cell within a row can contain a space (' '), a star ('*') to denote separation, a battleship ('⊙'), a miss ('x'), or a hit ('Ⓧ').
- Battleship Placement: User inputs for battleship locations are translated into coordinates that place '⊙' symbols on the board.
- Missile Strikes: Similar input handling is used for simulating missile strikes from the computer, updating the board with 'x' for misses and 'Ⓧ' for hits on player battleships.

This model supports the core gameplay loop, where the player and the computer take turns to set up and to attack the battleships based on this shared board structure.

## User Stories
- As a player, I want to be able to easily understand how to play the Battleships game so that I can get playing without prior experience.
- As a player, I want to see the game board clearly so that I can decide the positioning of my battleships.
- As a player, I want to know when I get hit or missed by my opponent's missiles so that I can learn the strategy my opponent is using to deploy their missiles.
- As a player, I want to know when I get hit or missed by my opponent's missiles so that I can adjust my ships positions accordingly in the next attempt.

## Design
### Responsive Design
The game is designed to be played in a terminal, ensuring a consistent experience across different environments.

### Color Scheme
The terminal's default color scheme is utilized for simplicity and accessibility.

### Font Choice
The game leverages the default terminal font to ensure maximum compatibility.

### Icons
- `⊙` represents the player's ships.
- `x` indicates a miss.
- `Ⓧ` marks a hit on a ship.

### Wireframes
N/A - The game is played in the terminal and does not have a graphical interface.

## Website Structure and Features
N/A - This project is a terminal-based game and does not have a web interface.

## Technologies Used
- VS Code for code editing
- Git and GitHub for version control
- Python3
- The `random` module for generating random events within the game.
- Heroku for hosting the deployed game version

## Testing and Validation
I performed testing for this application by doing the following:
1. Giving a range of valid and invalid values whenever prompted for user input.
2. Reviewing outputs in both my local terminal and the Code Institute Heroku terminal
3. Passing the final code through the Code Institute PEP8 Linter

### Bugs
#### Resolved Bugs
- Initial versions did not correctly identify invalid input ranges for both players. I resolved this by accounting for the empty, i.e., empty cells ' ' in the domain values for the column coordinates.
- Initial versions of the game did not correctly track the number of ships and missiles. I corrected this by initializing the counter outside the loop.
- The deployed version of my Battleships game was at one point in time not displaying the Game Analysis section well, i.e., this section was constantly truncated midway. I resolved this bug by adding new line escape characters (\n) on every print statement in the Game Analysis section.

#### Unresolved Bugs
- No unresolved bugs are known at the moment.

#### Validator Testing
- PEP8
    - No errors were returned from the [CI PEP8 validator](https://pep8ci.herokuapp.com/)

## Deployment
### Local Setup
1. Clone the repository to your local machine.
2. Ensure Python is installed.
3. Run `python3 run.py` or `python run.py` in your terminal to start the game.

To deploy:
1. Create a new Heroku app
2. Set the buildpacks to **Python** and **NodeJS** in this order
3. Link the Heroku app to the repository
4. Click on **Deploy**

## Contributions
Contributions are welcome. Players and users can fork the repository and open a pull request with their improvements.

## License
This project is licensed under the MIT License.

## Acknowledgement
### Code Inspiration
- The game logic was inspired by the classic Battleships board game.
- Code Institute provided the project template containing the deployment terminal

### Media
All game icons and symbols are created using standard Unicode characters.
