# Python Tkinter Tic-Tac-Toe

A simple, interactive Tic-Tac-Toe built with Python and its standard GUI library, Tkinter.

## Features

* **Graphical User Interface (GUI):** Built using Python's native Tkinter library.
* **Classic 3x3 Grid:** Standard Tic-Tac-Toe gameplay.
* **Two-Player Mode:** Designed for two human players (X and O) taking turns.
* **Turn Indication:** Displays whose turn it is (Player X or Player O).
* **Win Detection:** Automatically checks for win conditions (rows, columns, diagonals) after each move.
* **Draw Detection:** Detects when the game ends in a draw (board is full with no winner).
* **Game Over Notification:** Shows a message box indicating the winner or if it's a draw.
* **Play Again Option:** Asks players if they want to start a new game after one concludes.
* **Interactive Buttons:** Clickable grid cells for placing marks. Buttons are disabled after being clicked or when the game ends.
* **Responsive Layout:** The game grid scales with the window size.
  
## How to Run

1.  **Clone the repository or download the files:**
    ```bash
    git clone https://github.com/CreaTKeW/TicTacToe.git
    cd TicTacToe
    ```
    
2.  **Navigate to the directory** containing the files using your terminal or command prompt.

3.  **Run the main script:**
    ```bash
    python main.py
    ```

## Code Structure

* **`app.py`**: Contains the main `App` class which inherits from `tkinter.Tk`. This class handles:
    * Setting up the main window and layout.
    * Creating the grid buttons and status label.
    * Managing the game state (board, current player, game over status).
    * Handling button click events.
    * Checking for win/draw conditions.
    * Switching players.
    * Resetting the game.
* **`main.py`**: The entry point of the application. It imports the `App` class from `app.py` and starts the Tkinter main event loop (`app.mainloop()`), making the window visible and interactive.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/CreaTKeW/TicTacToe/issues) if you want to contribute.
