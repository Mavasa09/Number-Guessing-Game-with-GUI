import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 59)
        self.attempts = 0

        # Instructions label
        self.label = tk.Label(root, text='Guess a Number between 1 and 59', font=('Helvetica', 16))
        self.label.pack(pady=10)

        # Entry for user input
        self.entry = tk.Entry(root, font=('Helvetica', 16))
        self.entry.pack(pady=5)

        # Button to submit the guessed number
        self.guess_button = tk.Button(root, text='PLAY', command=self.check_guess, font=('Helvetica', 11))
        self.guess_button.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, font=('Helvetica', 11))
        self.reset_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(root, text='', font=('Helvetica', 11))
        self.feedback_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.secret_number:
                self.feedback_label.config(text='Too Low! Try Again')
            elif guess > self.secret_number:
                self.feedback_label.config(text='Too High! Try Again')
            else:
                messagebox.showinfo('Congratulations!', f'You guessed it in {self.attempts} attempts!')
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text='Please enter a valid number.')

    def reset_game(self):
        self.secret_number = random.randint(1, 59)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text='Guess a number between 1 and 59')

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
