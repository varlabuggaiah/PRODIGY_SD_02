# --- Guessing Game GUI Application ---

import tkinter as tk
from tkinter import ttk, messagebox
import random

class GuessingGame:
    """
    A class to encapsulate the Guessing Game application.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("500x450")
        self.root.configure(bg="#2c3e50") # Set a dark background color

        # --- Game Variables ---
        self.secret_number = 0
        self.attempts = 0

        # --- Style Configuration ---
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Configure styles for large, centered text
        self.style.configure('TLabel', background="#2c3e50", foreground="white", font=('Helvetica', 18))
        self.style.configure('TButton', font=('Helvetica', 14, 'bold'), padding=10)
        self.style.configure('TEntry', font=('Helvetica', 16), padding=10)
        
        # --- GUI Widgets ---
        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        """Create and place all the GUI elements."""
        
        # Main frame to hold all content
        main_frame = ttk.Frame(self.root, padding="30 30 30 30", style='TLabel')
        main_frame.pack(expand=True)

        # Title Label
        title_label = ttk.Label(main_frame, text="I'm thinking of a number between 1 and 100.", wraplength=400, justify="center")
        title_label.pack(pady=(0, 20))

        # Guess Entry
        self.guess_entry = ttk.Entry(main_frame, width=10, justify="center")
        self.guess_entry.pack(pady=10)
        # Bind the Enter key to the check_guess method
        self.guess_entry.bind('<Return>', self.check_guess_event)

        # Submit Guess Button
        self.submit_button = ttk.Button(main_frame, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        # Feedback Label
        self.feedback_label = ttk.Label(main_frame, text="Enter your guess to start!", font=('Helvetica', 16, 'italic'))
        self.feedback_label.pack(pady=20)

        # Attempts Label
        self.attempts_label = ttk.Label(main_frame, text="Attempts: 0", font=('Helvetica', 14))
        self.attempts_label.pack(pady=10)
        
        # Play Again Button (initially hidden)
        self.play_again_button = ttk.Button(main_frame, text="Play Again", command=self.start_new_game)
        # We use .pack_forget() later to hide it

    def start_new_game(self):
        """Resets the game state for a new round."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        # Reset UI elements
        self.feedback_label.config(text="A new game has started. Good luck!", foreground="white")
        self.attempts_label.config(text="Attempts: 0")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="normal") # Re-enable entry
        self.submit_button.config(state="normal") # Re-enable button
        
        # Hide the "Play Again" button if it's visible
        self.play_again_button.pack_forget()

    def check_guess_event(self, event):
        """Handler for the Enter key event."""
        self.check_guess()

    def check_guess(self):
        """Checks the user's guess against the secret number."""
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.", foreground="#3498db") # Blue for cool/low
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.", foreground="#e74c3c") # Red for hot/high
            else:
                self.feedback_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts!", foreground="#2ecc71") # Green for correct
                self.end_game()

        except ValueError:
            # Handle cases where the input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter a valid whole number.")
        finally:
            # Clear the entry box for the next guess
            self.guess_entry.delete(0, tk.END)
    
    def end_game(self):
        """Disables input and shows the 'Play Again' button."""
        self.guess_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.play_again_button.pack(pady=20)


# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()