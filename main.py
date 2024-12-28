# File: spinning_wheel_game.py

import tkinter as tk
from tkinter import ttk
import random


class SpinningWheelGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Wheel Game")
        self.current_wheel = 0
        self.selected_options = {}

        # Wheel data
        self.wheels = [
            {"name": "Time/Place", "options": ["Urban", "Rural", "Historical settings", "Extreme environment"]},
            {"name": "Character", "options": ["Main character", "Secondary character"]},
            {"name": "Type", "options": ["Female", "Male"]},
            {"name": "Type 2", "options": ["Evil", "Good"]},
            {"name": "Main Character Role", "options": ["The chosen one", "Misfit", "Ordinary", "King/queen",
                                                        "Brave knight", "Misunderstood teen", "A trickster"]},
        ]

        # Create UI
        self.label = ttk.Label(root, text="Welcome to the Spinning Wheel Game!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.spin_button = ttk.Button(root, text="Spin", command=self.spin_wheel)
        self.spin_button.pack(pady=20)

        self.result_label = ttk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def spin_wheel(self):
        # Handle spinning for the current wheel
        current_wheel_data = self.wheels[self.current_wheel]
        selected_option = random.choice(current_wheel_data["options"])
        self.selected_options[current_wheel_data["name"]] = selected_option

        self.result_label.config(text=f"{current_wheel_data['name']} selected: {selected_option}")

        # Determine next wheel logic
        self.current_wheel += 1
        if self.current_wheel == 4 and self.selected_options["Character"] == "Main character" and \
                self.selected_options["Type 2"] == "Good":
            self.current_wheel = 4  # Go to Main Character Role
        elif self.current_wheel >= len(self.wheels):
            self.end_game()
            return

        next_wheel_name = self.wheels[self.current_wheel]["name"]
        self.label.config(text=f"Spin the {next_wheel_name} Wheel!")

    def end_game(self):
        summary = "\n".join([f"{key}: {value}" for key, value in self.selected_options.items()])
        self.label.config(text="Game Over! Here are your results:")
        self.result_label.config(text=summary)
        self.spin_button.config(state="disabled")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    game = SpinningWheelGame(root)
    root.mainloop()
