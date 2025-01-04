import unittest
from blackjack import Card, Deck, Hand, hit

class TestBlackjack(unittest.TestCase):

    def test_opening_hand(self):
        # Test that the player is dealt two cards in the opening hand
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        self.assertEqual(len(player_hand.cards), 2)

    def test_hit(self):
        # Test that hitting adds another card and updates the score
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        initial_cards = len(player_hand.cards)
        initial_value = player_hand.value
        hit(deck, player_hand)
        self.assertEqual(len(player_hand.cards), initial_cards + 1)
        self.assertNotEqual(player_hand.value, initial_value)

    def test_stand(self):
        # Test that standing does not add more cards and evaluates the score
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        initial_cards = len(player_hand.cards)
        initial_value = player_hand.value
        # simulate stand by not calling hit
        self.assertEqual(len(player_hand.cards), initial_cards)
        self.assertEqual(player_hand.value, initial_value)

    def test_valid_hand(self):
        # Test that a hand is valid if the score is 21 or less
        hand = Hand()
        hand.add_card(Card('Hearts', 'Ten'))
        hand.add_card(Card('Hearts', 'Ace'))
        self.assertTrue(hand.value <= 21)
        hand.add_card(Card('Clubs', 'Nine'))
        self.assertTrue(hand.value <= 21)

    def test_bust(self):
        # Test that a hand is bust if the score is 22 or more
        hand = Hand()
        hand.add_card(Card('Hearts', 'Ten'))
        hand.add_card(Card('Hearts', 'King'))
        hand.add_card(Card('Hearts', 'Three'))
        self.assertTrue(hand.value > 21)

    def test_blackjack_with_king_and_ace(self):
        # Test that a hand with a king and an ace scores 21
        hand = Hand()
        hand.add_card(Card('Hearts', 'King'))
        hand.add_card(Card('Hearts', 'Ace'))
        self.assertEqual(hand.value, 21)

    def test_blackjack_with_king_queen_and_ace(self):
        # Test that a hand with a king, queen, and an ace scores 21
        hand = Hand()
        hand.add_card(Card('Hearts', 'King'))
        hand.add_card(Card('Hearts', 'Queen'))
        hand.add_card(Card('Hearts', 'Ace'))
        self.assertEqual(hand.value, 21)

    def test_blackjack_with_nine_and_two_aces(self):
        # Test that a hand with a nine and two aces scores 21
        hand = Hand()
        hand.add_card(Card('Hearts', 'Nine'))
        hand.add_card(Card('Hearts', 'Ace'))
        hand.add_card(Card('Spades', 'Ace'))
        self.assertEqual(hand.value, 21)

if __name__ == '__main__':
    unittest.main()

