import random  # Import the random module to shuffle the deck

# Define the suits, ranks, and values of the cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Four suits in a deck
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Ranks of cards
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  # Values of cards

playing = True  # Variable to control the game flow

# Class to represent a card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # Initialize the suit of the card
        self.rank = rank  # Initialize the rank of the card

    def __str__(self):
        return self.rank + ' of ' + self.suit  # Return the card's rank and suit as a string

# Class to represent a deck of cards
class Deck:
    def __init__(self):
        self.deck = []  # Create an empty deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # Add all cards to the deck

    def __str__(self):
        deck_comp = ''  # Initialize an empty string to hold the deck composition
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # Add each card to the string
        return 'The deck has: ' + deck_comp  

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle the deck

    def deal(self):
        return self.deck.pop()  # Deal a card from the deck

# Class to represent a hand of cards
class Hand:
    def __init__(self):
        self.cards = []  # Create an empty hand
        self.value = 0  # Initialize the value of the hand
        self.aces = 0  # Initialize the count of aces

    def add_card(self, card):
        self.cards.append(card)  # Add a card to the hand
        self.value += values[card.rank]  # Update the value of the hand
        if card.rank == 'Ace':
            self.aces += 1  # Count the ace
        self.adjust_for_ace()  # Ensure aces are adjusted for

    def adjust_for_ace(self):
        # Adjust the value of the hand if there are aces and the value exceeds 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Function to hit a card
def hit(deck, hand):
    hand.add_card(deck.deal())  # Add a card to the hand
    hand.adjust_for_ace()  # Adjust for aces

# Function to handle the player's choice to hit or stand
def hit_or_stand(deck, hand):
    global playing

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")  # Ask the player to hit or stand

        if ask[0].lower() == 'h':
            hit(deck, hand)  # Hit if the player chooses 'h'
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")  # Stand if the player chooses 's'
            playing = False
        else:
            print("You are confusing me! Please try again!")  # Handle invalid input
            continue
        break

# Function to show some of the dealer's cards and all of the player's cards
def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")  # Hide the dealer's first card
    print("", dealer.cards[1])  # Show the dealer's second card
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')  # Show all of the player's cards

# Function to show all of the dealer's and player's cards
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')  # Show all of the dealer's cards
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')  # Show all of the player's cards
    print("Player's Hand =", player.value)

# Function for when the player busts
def player_busts(player, dealer):
    print("PLAYER BUSTS!")  # Print a message indicating that the player busts

# Function for when the player wins
def player_wins(player, dealer):
    print("PLAYER WINS!")  # Print a message indicating that the player wins
    print("WELL DONE!!!!!!!!! YOU WIN!!!!!!!")  # Additional message to congratulate the player

# Function for when the dealer busts
def dealer_busts(player, dealer):
    print("DEALER BUSTS!")  # Print a message indicating that the dealer busts

# Function for when the dealer wins
def dealer_wins(player, dealer):
    print("DEALER WINS!")  # Print a message indicating that the dealer wins

# Function for a push (tie) between the player and dealer
def push(player, dealer):
    print("You and Dealer TIE!")  # Print a message indicating a push

# Main game loop
while True:
    print("Time to test your luck at Blackjack!")

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal initial cards to player and dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Show initial hands
    show_some(player_hand, dealer_hand)

    # Player's turn
    while playing:
        hit_or_stand(deck, player_hand)  # Prompt player to hit or stand
        show_some(player_hand, dealer_hand)  # Show cards

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)  # Player busts
            break

    # Dealer's turn if player hasn't busted
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)  # Dealer hits until their hand value is at least 17

        show_all(player_hand, dealer_hand)  # Show all cards

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)  # Dealer busts
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)  # Dealer wins
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)  # Player wins
        elif dealer_hand.value == player_hand.value: 
            push(player_hand, dealer_hand) 

    # Ask if the player wants to play again
    new_game = input("\nWant to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue  # Start a new game
    else:
        print("\nIt was fun playing with you! See you soon!")  # End the game
        break

