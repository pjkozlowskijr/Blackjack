import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \2662"]
card_name = ["A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
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
class Card():
    def __init__(self,card_name,card_value):
        self.card_name = card_name
        self.card_value = card_value

    def __str__(self):
        return self.rank + 'of' + self.suit


class Deck:
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for card_name in card_name:
                self.deck.append(Card(suit, card_name))

    def __str__(self):
        deck_comp = " "  
        for card in self.deck:
            deck_comp += "\n " + card.__str__()  
        return "Your deck contains:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Person():
    def __init__(self):
        self.hand=[]
        self.score = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card_value[card.card_name]
        if card_value == "A":
            self.aces+=1



    def ace_adjust(self):
        pass

class BlackJack():
    def __init__(self):
        self.card = Card(Card.suit, Card.card)
        self.deck = Deck()
        dealer = Person()
        player = Person()

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