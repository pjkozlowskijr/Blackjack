import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \u2662"]
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
            print("\nDealer wins. You lose. Better luck next time.")
            self.play_again()
        elif self.dealer.score == self.player.score:
            print("\nIt's a push. No one wins.")
            self.play_again()
        else: 
            print("\nYou win! Congrats!")
            self.play_again()
    
    def check_dealer_score(self):
        self.show_all_cards()
        if self.dealer.score < 17:
            print("\nDealer takes card since score under 17.")
            self.dealer.add_card(self.deck.deal())
            self.check_dealer_score()
        elif self.dealer.score > 21:
            self.dealer.ace_adjust()
            if self.dealer.score > 21:
                print("\nDealer busts! You win! Congrats!")
                self.play_again()
            else:
                print("\nDealer Ace was adjusted from 11 points to 1 point, taking total score back under 21.")
                self.check_dealer_score()
        else:
            self.compare_scores()

    def check_player_score(self):
        while self.player.score < 21:
            hit_or_stay = input("\nDo you want to hit ['h'] or stay ['s']? ").strip().lower()
            if hit_or_stay == "h":
                clear_screen()
                self.player.add_card(self.deck.deal())
                self.show_cards()
                if self.player.score > 21:
                    self.player.ace_adjust()
                    if self.player.score > 21:
                        print("\nYou busted! Try again.")
                        self.play_again()
                    else:
                        print("\nYour Ace was adjusted from 11 points to 1 point, taking total score back under 21.")
                        self.show_cards()
                        continue
            elif hit_or_stay == "s":
                clear_screen()
                break  
            else:
                print("Invalid entry. Try again.")

    def start_game(self):
        clear_screen()
        print("Welcome to Patrick and Kyle's blackjack table. Good luck!")
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.ace_adjust()
        self.show_cards()
        if self.player.score == 21:
            print("\nYou have BLACKJACK!!! You win! Congrats!")
            self.play_again()

    def play_game(self):
        self.start_game()
        self.check_player_score()
        self.check_dealer_score()

    def play_again(self):
        again = input("\nDo you want to play again? Y/N ").strip().lower()
        if again == "y":
            self.deck = Deck()
            self.deck.shuffle()
            self.dealer = Person()
            self.player = Person()
            self.play_game()

def main():
    game = Blackjack()
    game.play_game()

if __name__ == "__main__":
    main()