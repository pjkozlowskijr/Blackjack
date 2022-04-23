import random
import os
from tkinter import Y

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \2662"]
card_name = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
card_value = {
    "Ace": 11,
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
    def __init__(self, suit, card_name, card_value):
        self.suit = suit
        self.card_name = card_name
        self.card_value = card_value

    def __str__(self):
        return self.card_name + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for card in card_name:
                self.deck.append(Card(suit, card, card_value[card]))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

class Person:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card_value[card.card_name]
        if card.card_name == "Ace":
            self.aces += 1

    def ace_adjust(self):
        if self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Person()
        self.player = Person()
    
    def show_cards(self):
        print("\nYour hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:\n<HIDDEN CARD>")
        for ind in range(1, len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")
            

    def show_all_cards(self):
        print("\nYour hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:")
        for ind in range(len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")
        print("Dealer score:", self.dealer.score)

    def compare_scores(self):
        if self.dealer.score > self.player.score:
            print("dealers wins\n you lose")
        elif self.dealer.score == self.player.score:
            print('its a push') 
        else: 
            print('player wins dealer loses')
        play_again = Blackjack()
        play_again.play_game()
    
    def check_dealer_score(self):
        self.show_all_cards()
        
        if self.dealer.score <17:
            self.dealer.add_card(self.deck.deal())
            self.check_dealer_score()
        elif self.dealer.score > 21:
            self.dealer.ace_adjust()
            if self.dealer.score > 21:
                print('player wins')
                play_again = Blackjack()
                play_again.play_game()
        else:
            self.compare_scores() 
            
            
        # play_again = Blackjack()
        # play_again.play_game()
        
    def play_game(self):
        action = input("Do you want to play a game of blackjack? Y/N ").strip().lower()
        if action == "y":
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())
            self.show_cards()
            if self.player.score == 21:
                print("You have BLACKJACK!!! You win! Congrats!")
                play_again = Blackjack()
                play_again.play_game()
        elif action == "n":
            print("Have a great day.")
            
        else:
            print("Invalid entry. Try again.")
            self.play_game()

        
        while self.player.score < 21:
            hit_or_stay = input("Do you want to hit ['h'] or stay ['s']? ").strip().lower()
            if hit_or_stay == "h":
                self.player.add_card(self.deck.deal())
                self.show_cards()
                if self.player.score > 21:
                    self.player.ace_adjust()
                    if self.player.score > 21:
                        print("You busted! Try again.")
                        play_again = Blackjack()
                        play_again.play_game()
                    else:
                        self.show_cards()
                        continue
            elif hit_or_stay == "s":
                self.check_dealer_score()
                break 
                
            else:
                print("Invalid entry. Try again.")

            
game = Blackjack()
game.play_game()
