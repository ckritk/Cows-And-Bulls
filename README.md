# CowsAndBulls
An application for the Cows and Bulls game. Cows and Bulls is a number guessing game where the player tries to guess a secret code within a limited number of attempts. Each guess results in feedback in the form of "cows" (correct digits in the correct position) and "bulls" (correct digits in the wrong position). The player wins by correctly guessing the entire code.

## Project Structure
**Main_Game_Func.py:** Contains the main game logic and the GUI setup using Tkinter. It includes functions to start the game, handle user inputs, and update game statistics.

**stfunc.py:** Provides functionalities to display game statistics, such as the number of games played, won, lost, and the best time records.

**ProgrammableTimerApp.py:** Implements a timer used in the game to keep track of the duration of each game.

**candb.sql:** Contains the schema and initial data for the MySQL database used to store game statistics.

## How to Run the Code
### Set up the MySQL Database:

Open the candb.sql file in a MySQL-compatible IDE (like MySQL Workbench) and run the script to create the database and the data table.
### Update MySQL Connector Credentials:

In Main_Game_Func.py and stfunc.py, update the username and password fields in the MySQL connector section with your MySQL database credentials.

_db = c.connect(host='127.0.0.1', user='your_username', password='your_password', database='candb')_
### Run the Main Game:

Execute the Main_Game_Func.py file using Python then call Main_Game_Func() in the console to start the game.

