# Mini Battleships Game README

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
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
- [Deployment](#deployment)
  - [Local Setup](#local-setup)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgement](#acknowledgement)
  - [Code Inspiration](#code-inspiration)
  - [Media](#media)

## Introduction
The Mini Battleships Game is a strategy type guessing game designed for two players: the PLAYER (you) and the OPPONENT (computer).

## Project Overview
This project simulates the classic Battleships game in a simplified version. Players take turns to guess the locations of each other's ships on a hidden board with the aim of "sinking" all the opponent's ships.

## User Stories
- As a player, I want to be able to easily understand how to play the game.
- As a player, I want to see the game board clearly so that I can make informed guesses.
- As a player, I want to know when I hit or miss an opponent's ship.

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
### Bugs
#### Resolved Bugs
- Initial versions did not correctly check for valid input ranges for both players.

#### Unresolved Bugs
- No unresolved bugs at the moment.

## Deployment
### Local Setup
1. Clone the repository to your local machine.
2. Ensure Python is installed.
3. Run `python3 run.py` in your terminal to start the game.

## Contributions
Contributions are welcome. Please fork the repository and open a pull request with your improvements.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgement
### Code Inspiration
The game logic was inspired by the classic Battleships board game.

### Media
All game icons and symbols are created using standard Unicode characters.
