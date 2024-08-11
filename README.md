# CowsAndBulls

## Overview
Cows and Bulls is a number guessing game where the player tries to guess a secret code within a limited number of attempts. Each guess provides feedback in the form of "cows" (correct digits in the correct position) and "bulls" (correct digits in the wrong position). The player wins by correctly guessing the entire code.

## Tech Stack
- **Python:** Programming language used for game logic and GUI.
- **Tkinter:** GUI library used for the game's user interface.
- **MySQL:** Database system used to store game statistics.

## Features
- **Main Game Logic:** Core game functionality and user interface implemented with Tkinter.
- **Game Statistics:** Tracks and displays game statistics, including games played, won, lost, and best times.

## Usage

### Set up the MySQL Database
1. Open the `candb.sql` file in a MySQL-compatible IDE (such as MySQL Workbench).
2. Run the script to create the database and data table:
   ```bash
   mysql -u your_username -p < candb.sql
   ```

### Update MySQL Connector Credentials
1. Open `Main_Game_Func.py` and `stfunc.py`.
2. Update the MySQL connector credentials with your database details:
   ```python
   db = c.connect(host='127.0.0.1', user='your_username', password='your_password', database='candb')
   ```

### Run the Main Game
1. Execute the `Main_Game_Func.py` file using Python:
   ```bash
   python Main_Game_Func.py
   ```
2. Start the game by calling the `Main_Game_Func()` function in the console:
   ```python
   Main_Game_Func()
   ```

## Contributions
Contributions to the Cows and Bulls project are welcome. If you'd like to contribute, please submit a pull request with your changes, and we'll review it for inclusion in the project.

We appreciate your contributions and look forward to collaborating with you!
