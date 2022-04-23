import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \2662"]
card_name: ["A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
card_value = {
    "A": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6, 
    "Seven": 7, 
    "Eight": 8,
    "Nine": 9, 
    "Ten": 10, 
    "Jack": 10, 
    "Queen": 10, 
    "King": 10,
}

class Card:
    def __init__(self, suit, card_name, card_value):
        self.suit = suit
        self.card_name = card_name
        self.card_value = card_value

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card in card_name:
                self.deck.append(Card(suit, card, card_value[card]))

class Dealer:
    def __init__(self):
        self.dealer_hand = []
        self.dealer_score = 0

    def add_card(self):
        added_card = random.choice(Deck.deck)
        self.dealer_hand.append(added_card)
        self.dealer_score += added_card.card_value

    def stand(self):
        pass
        
class Player:
    def __init__(self):
        self.player_hand = []
        self.player_score = 0

    def hit(self):
        pass

    def stand(self):
        pass

class Blackjack:
    def __init__(self):
        self.card = Card(Card.suit, Card.card)
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def play_game(self):
        action = input("Do you want to play a game of blackjack? Y/N ").strip().lower()
        if action == "y":
            # Add card player
            # Add card dealer
            # Add card player
            # Add card dealer
            # Print "You have x & y in your hand. Your total is z." 
            # Check for player blackjack.
            # If blackjack...player wins
            # If no blackjack: Do you want to hit or stand?"
            pass
