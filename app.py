import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tic Tac Toe')
        self.geometry('350x400')
        self.player = "X"
        self.game_over = False

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 16, 'bold'))

        # Store button references and board state
        self.buttons = [[None for i in range(3)] for j in range(3)]
        self.board_state = [['', '', ''], ['', '', ''], ['', '', '']]

        # Configure main window expansion
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) # Grid area
        self.rowconfigure(1, weight=0) # Status label area

        # Main frame for the game grid
        self.mainframe = ttk.Frame(self, padding='5 5 5 5')
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Configure grid expansion inside the mainframe
        for i in range(3):
            self.mainframe.columnconfigure(i, weight=1)
            self.mainframe.rowconfigure(i, weight=1)

        # Status label
        self.status_label = ttk.Label(self, text=f"Player {self.player}'s Turn")
        self.status_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # Create the grid buttons
        self.create_grid_widgets()

    def create_grid_widgets(self):
        """Creates the grid buttons and assigns their commands."""
        for r in range(3):
            for c in range(3):
                # Use lambda to pass current row and column to the handler function.
                button = ttk.Button(self.mainframe, text='',
                                   command=lambda r=r, c=c: self.on_button_click(r, c))
                button.grid(column=c, row=r, sticky=(tk.N, tk.S, tk.E, tk.W), padx=2, pady=2)

                # Store button reference
                self.buttons[r][c] = button

    def on_button_click(self, r, c):
        """Handles a button click event at cell (r,c)."""
        # Check if the game is not over and the cell is empty
        if not self.game_over and self.board_state[r][c] == '':
            current_player = self.player
            # Update button text and internal board state
            self.buttons[r][c].config(text=current_player)
            self.board_state[r][c] = current_player

            # Disable the clicked button
            self.buttons[r][c].config(state=tk.DISABLED)

            # Check if this move ended the game
            game_ended_this_turn = False
            result_message = ""
            winner = None

            if self.check_win():
                self.game_over = True
                game_ended_this_turn = True
                winner = current_player
                result_message = f"Player {winner} wins!"
                self.status_label.config(text=f"Player {winner} Wins!")
                self.disable_all_buttons()

            elif self.check_draw():
                self.game_over = True
                game_ended_this_turn = True
                result_message = "It's a draw!"
                self.status_label.config(text="It's a Draw!")
                self.disable_all_buttons()

            # --- Ask to play again if the game just ended ---
            if game_ended_this_turn:
                # First show the result
                messagebox.showinfo("Game Over!", result_message)
                # Then ask to play again
                play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
                if play_again:
                    self.reset_game()

            else: # If game did not end this turn, switch player
                self.switch_player()
                self.status_label.config(text=f"Player {self.player}'s Turn")

    def switch_player(self):
        """Switches the active player between X and O."""
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def check_win(self):
        """Checks if the current board state has a winner."""
        # Check rows
        for r in range(3):
            if self.board_state[r][0] == self.board_state[r][1] == self.board_state[r][2] != '':
                return True
        # Check columns
        for c in range(3):
            if self.board_state[0][c] == self.board_state[1][c] == self.board_state[2][c] != '':
                return True
        # Check diagonals
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] != '':
            return True
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] != '':
            return True
        # No winner found
        return False

    def check_draw(self):
        if self.check_win(): # Cannot be a draw if someone won
            return False

        # Check if any cell is still empty
        for r in range(3):
            for c in range(3):
                if self.board_state[r][c] == '':
                    return False # Found an empty cell, game is not a draw yet
        # No empty cells and no winner -> Draw
        return True

    def disable_all_buttons(self):
        for r in range(3):
            for c in range(3):
                 if self.buttons[r][c]:
                    self.buttons[r][c].config(state=tk.DISABLED)

    def reset_game(self):
        """Resets the game board to the initial state."""
        self.player = "X" # Reset starting player
        self.game_over = False # Reset game over flag
        self.board_state = [['', '', ''], ['', '', ''], ['', '', '']] # Clear internal state

        # Reset buttons appearance and state
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]:
                    self.buttons[r][c].config(text='', state=tk.NORMAL) # Clear text, re-enable

        # Update status label
        self.status_label.config(text=f"Player {self.player}'s Turn")