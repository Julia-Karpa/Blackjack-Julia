# Blackjack Game
### Overview
This is a simple text-based Blackjack game written in Python. In this game, players try to get a hand value as close to 21 as possible without exceeding it.

### Card Values
Number cards (2-10) are worth their face value.

Face cards (Jack, Queen, King) are worth 10 points.

Aces can be worth either 1 or 11 points, depending on which value is more beneficial for the hand.

### Setup
Ensure you have Python installed on your system.

Download the code file.

### Running the Game
To start the game, run the Python script:
python blackjack.py

### Game Flow
Initialization: Create and shuffle the deck.

Initial Deal: Deal two cards to the player and the dealer.

Player's Turn: The player can hit or stand.

Dealer's Turn: The dealer draws cards until their hand value is at least 17.

Determine Outcome: Compare the player's and dealer's hands to determine the winner.

The goal is to have a hand value closer to 21 than the dealer without exceeding 21.

### Running Tests
Unit tests are provided to ensure the game logic is functioning correctly. To run the tests, execute the following command:
python -m unittest test_blackjack.py


