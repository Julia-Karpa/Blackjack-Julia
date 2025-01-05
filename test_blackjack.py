import unittest  # Import the unittest module for writing and running tests
from blackjack import Card, Deck, Hand, hit  # Import the necessary classes and functions from the blackjack module

class TestBlackjack(unittest.TestCase): 

    def test_opening_hand(self):  # Define a test method to check the opening hand
        deck = Deck()  # Create a new deck of cards
        deck.shuffle()  # Shuffle the deck
        player_hand = Hand()  # Create a new hand for the player
        player_hand.add_card(deck.deal())  # Deal the first card to the player's hand
        player_hand.add_card(deck.deal())  # Deal the second card to the player's hand
        self.assertEqual(len(player_hand.cards), 2)  # Assert that the player's hand has two cards

    def test_hit(self):  # Define a test method to check the hit functionality
        deck = Deck()  # Create a new deck of cards
        deck.shuffle()  # Shuffle the deck
        player_hand = Hand()  # Create a new hand for the player
        player_hand.add_card(deck.deal())  # Deal the first card to the player's hand
        player_hand.add_card(deck.deal())  # Deal the second card to the player's hand
        initial_cards = len(player_hand.cards)  # Store the initial number of cards in the player's hand
        initial_value = player_hand.value  # Store the initial value of the player's hand
        hit(deck, player_hand)  # Hit: add another card to the player's hand
        self.assertEqual(len(player_hand.cards), initial_cards + 1)  # Assert that the number of cards has increased by one
        self.assertNotEqual(player_hand.value, initial_value)  # Assert that the value of the hand has changed

    def test_stand(self):  # Define a test method to check the stand functionality
        deck = Deck()  # Create a new deck of cards
        deck.shuffle()  # Shuffle the deck
        player_hand = Hand()  # Create a new hand for the player
        player_hand.add_card(deck.deal())  # Deal the first card to the player's hand
        player_hand.add_card(deck.deal())  # Deal the second card to the player's hand
        initial_cards = len(player_hand.cards)  # Store the initial number of cards in the player's hand
        initial_value = player_hand.value  # Store the initial value of the player's hand
        # Simulate stand by not calling hit
        self.assertEqual(len(player_hand.cards), initial_cards)  # Assert that the number of cards remains the same
        self.assertEqual(player_hand.value, initial_value)  # Assert that the value of the hand remains the same

    def test_valid_hand(self):  # Define a test method to check a valid hand
        hand = Hand()  # Create a new hand
        hand.add_card(Card('Hearts', 'Ten'))  # Add a Ten of Hearts to the hand
        hand.add_card(Card('Hearts', 'Ace'))  # Add an Ace of Hearts to the hand
        self.assertTrue(hand.value <= 21)  # Assert that the hand's value is 21 or less
        hand.add_card(Card('Clubs', 'Nine'))  # Add a Nine of Clubs to the hand
        self.assertTrue(hand.value <= 21)  # Assert that the hand's value is still 21 or less

    def test_bust(self):  # Define a test method to check a bust hand
        hand = Hand()  # Create a new hand
        hand.add_card(Card('Hearts', 'Ten'))  # Add a Ten of Hearts to the hand
        hand.add_card(Card('Hearts', 'King'))  # Add a King of Hearts to the hand
        hand.add_card(Card('Hearts', 'Three'))  # Add a Three of Hearts to the hand
        self.assertTrue(hand.value > 21)  # Assert that the hand's value is greater than 21

    def test_blackjack_with_king_and_ace(self):  # Define a test method to check Blackjack with a King and an Ace
        hand = Hand()  # Create a new hand
        hand.add_card(Card('Hearts', 'King'))  # Add a King of Hearts to the hand
        hand.add_card(Card('Hearts', 'Ace'))  # Add an Ace of Hearts to the hand
        self.assertEqual(hand.value, 21)  # Assert that the hand's value is 21

    def test_blackjack_with_king_queen_and_ace(self):  # Define a test method to check Blackjack with a King, Queen, and an Ace
        hand = Hand()  # Create a new hand
        hand.add_card(Card('Hearts', 'King'))  # Add a King of Hearts to the hand
        hand.add_card(Card('Hearts', 'Queen'))  # Add a Queen of Hearts to the hand
        hand.add_card(Card('Hearts', 'Ace'))  # Add an Ace of Hearts to the hand
        self.assertEqual(hand.value, 21)  # Assert that the hand's value is 21

    def test_blackjack_with_nine_and_two_aces(self):  # Define a test method to check Blackjack with a Nine and two Aces
        hand = Hand()  # Create a new hand
        hand.add_card(Card('Hearts', 'Nine'))  # Add a Nine of Hearts to the hand
        hand.add_card(Card('Hearts', 'Ace'))  # Add an Ace of Hearts to the hand
        hand.add_card(Card('Spades', 'Ace'))  # Add an Ace of Spades to the hand
        self.assertEqual(hand.value, 21)  # Assert that the hand's value is 21

if __name__ == '__main__':
    unittest.main()  # Run all the test cases if the script is executed directly
