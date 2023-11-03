#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
"""
import random

# Función para jugar una ronda del juego
def play_round():
    user_input = input("Choose rock, paper, or scissors: ").lower()
    
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please enter a valid input.")
        return None

    computer_input = random.choice(["rock", "paper", "scissors"])
    print("Computer chose: " + computer_input)

    if user_input == computer_input:
        return "Tie"
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "scissors" and computer_input == "paper") or \
         (user_input == "paper" and computer_input == "rock"):
        return "You win"
    else:
        return "You lose"

# Función para jugar el juego completo
def play_game():
    wins = 0
    rounds = 0

    while True:
        result = play_round()
        if result == "You win":
            wins += 1
        rounds += 1
        print(result)  # Muestra el resultado de la ronda
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Game over! You won", wins, "out of", rounds, "rounds.")

# Iniciar el juego
if __name__ == "__main__":
    play_game()
