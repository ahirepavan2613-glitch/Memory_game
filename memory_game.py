import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match Game")
        self.root.resizable(False, False)

        self.symbols = ["🐶", "🐱", "🦊", "🐼",
                        "🐸", "🐵", "🦁", "🐯"]

        self.moves = 0
        self.matches = 0
        self.first_card = None
        self.second_card = None
        self.locked = False

        self.moves_label = tk.Label(
            root, text="Moves: 0", font=("Arial", 14)
        )
        self.moves_label.grid(row=0, column=0, columnspan=4, pady=10)

        self.buttons = []
        self.create_board()

        restart = tk.Button(
            root,
            text="New Game",
            font=("Arial", 12),
            command=self.new_game
        )
        restart.grid(row=5, column=0, columnspan=4, pady=10)

    def create_board(self):
        cards = self.symbols * 2
        random.shuffle(cards)

        for i, symbol in enumerate(cards):
            button = tk.Button(
                self.root,
                text="?",
                font=("Arial", 24),
                width=4,
                height=2,
                command=lambda i=i, symbol=symbol: self.flip_card(i, symbol)
            )
            button.grid(
                row=(i // 4) + 1,
                column=i % 4,
                padx=5,
                pady=5
            )
            self.buttons.append(button)

    def flip_card(self, index, symbol):
        if self.locked:
            return

        button = self.buttons[index]

        if button["text"] != "?":
            return

        button.config(text=symbol)

        if self.first_card is None:
            self.first_card = (index, symbol)

        else:
            self.second_card = (index, symbol)
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            self.locked = True

            self.root.after(700, self.check_match)

    def check_match(self):
        first_index, first_symbol = self.first_card
        second_index, second_symbol = self.second_card

        if first_symbol == second_symbol:
            self.matches += 1

            if self.matches == len(self.symbols):
                self.moves_label.config(
                    text=f"You won! 🎉 Moves: {self.moves}"
                )

        else:
            self.buttons[first_index].config(text="?")
            self.buttons[second_index].config(text="?")

        self.first_card = None
        self.second_card = None
        self.locked = False

    def new_game(self):
        for button in self.buttons:
            button.destroy()

        self.buttons = []
        self.moves = 0
        self.matches = 0
        self.first_card = None
        self.second_card = None
        self.locked = False

        self.moves_label.config(text="Moves: 0")
        self.create_board()


root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
