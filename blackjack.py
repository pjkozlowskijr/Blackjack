import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \2662"]
cards = {
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
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

class Deck:
    def __init__(self):
        deck = []
        for suit in suits:
            for card in cards:
                deck.append(Card(suit, card))

    def shuffle(self):
        pass

class Dealer:
    def __init__(self):
        dealer_hand = []
        dealer_score = 0

    def deal(self):
        pass

    def hit(self):
        pass

    def stand(self):
        pass
        
class Player:
    def __init__(self):
        player_hand = []
        player_score = 0

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
        action = input("Do you want to play a game of blackjack? Y/N ")

