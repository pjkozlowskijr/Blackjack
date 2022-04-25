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

class Betting():
    def __init__(self):
        self.bank = 100
        self.wager = 0
        self.borrow_money = ""

    def placebet(self):
        wager = input(f"Your current bank is: ${self.bank}. How much would you like to wager? ")
        if int(wager) > 0:
            self.wager = int(wager)
            clear_screen
            print(f"\nThis is where the fun begins. Let's see what you can do with the ${self.wager} you risked.")
            if int(wager) > self.bank:
                print(f"You only have ${self.bank} in your bank. Stop being broke and get more money if you wanna bet that much.")
        elif wager == "quit":
            self.wager = "quit"
        else:
            clear_screen()
            print("Invalid entry. Please enter only whole numbers as digits.\n")
            self.placebet()
       
    def losingbet(self):
        self.bank = self.bank - self.wager
        print(f"\nDealer wins. You lost ${self.wager}. Better luck next time.")
        if self.bank == 0:
            while self.borrow_money == "":
                print(f"\nYou\'re broke. Your bank is ${self.bank}.")
                self.borrow_money = input("\nWould you like to borrow $100 from a loan shark? Y/N ").lower().strip()
                if self.borrow_money == 'y':
                    new_game = Blackjack()
                    new_game.play_game()
                elif self.borrow_money == 'n' or self.borrow_money == "quit":
                    clear_screen()
                else:
                    print("Invalid response. Please try again")
                    self.borrow_money = ""

    def winningbet(self):
        self.bank = self.bank + self.wager
        print(f"\nYou won ${self.wager}! Congrats!")
        
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
        self.betting = Betting()
        self.playing = None

    def welcome(self):
        print("Welcome to Patrick & Kyle\'s blackjack table! Good luck!")
        help_or_play = input("\nTo start playing, enter 'play'. To see the help menu, type 'help'. ").strip().lower()
        if help_or_play == "play":
            clear_screen()
            self.play_game()
        elif help_or_play == "help":
            self.help()
        elif help_or_play == "quit":
            self.goodbye()
        else:
            print("\nInvalid entry. Try again.\n")
            self.welcome()

    def help(self):
        clear_screen()
        print("Help Menu")
        print("\nYou may quit at any time by typing 'quit' into the input.")
        print("\n----------------------------------------------------------------------------------")
        print("\nRules of Blackjack")
        print("\n- Player starts with $100 in your bank.")
        print("- Try to beat the dealer by getting as close to 21 as possible without going over.")
        print("- Bust = going over 21 and automatic loss.")
        print("- Player and dealer each start with two cards. One of the dealer's cards is hidden.")
        print("- If player's first two cards total 21, that's Blackjack and an automatic win.")
        print("- If not, player can hit or stay.")
        print("\t- Hit = take another card.")
        print("\t- Stay = keep total and end turn.")
        print("- Dealer's hidden card is revealed once player stays.")
        print("- If dealer total less than 17, dealer must hit.")
        print("- If dealer total 17 or greater, dealer must stay.")
        print("- If neither player nor dealer busts, highest total wins.")
        print("- Card point values:")
        print("\t- Ace = 11 (NOTE: If score goes above 21, Ace value adjusted to 1.)")
        print("\t- King, Queen, Jack = 10")
        print("\t- All others = face value (i.e. Two = 2, Three = 3, etc.)")
        print("- There is no splitting pairs, doubling down, or insurance in this version.\n")
        self.welcome()

    def play_game(self):
        self.playing = True
        if self.playing == True:
            self.betting.placebet()
        if self.playing == True and self.betting.wager != "quit":
            self.start_game()
        else:
            self.goodbye()
        if self.playing == True:
            self.show_cards()
        if self.playing == True:
            self.check_player_score()
        if self.playing == True:
            self.check_dealer_score()

    def start_game(self):
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.ace_adjust()

    def show_cards(self):
        print("\nYour hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:\n<HIDDEN CARD>")
        for ind in range(1, len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")

    def check_player_score(self):
        if self.player.score == 21:
            print(f"\nYou have BLACKJACK!!! You won ${self.betting.wager}! Congrats!")
            self.betting.winningbet()
            self.play_again()
        else:
            while self.player.score < 21:
                hit_or_stay = input("\nDo you want to hit ['h'] or stay ['s']? ").strip().lower()
                if hit_or_stay == "h":
                    clear_screen()
                    self.player.add_card(self.deck.deal())
                    self.show_cards()
                    if self.player.score > 21:
                        self.player.ace_adjust()
                        if self.player.score > 21:
                            print("You busted!")
                            self.playing = False
                            self.betting.losingbet()
                            self.play_again()
                        else:
                            print("\nYour Ace was adjusted from 11 points to 1 point, taking total score back under 21.")
                            self.show_cards()
                            continue
                elif hit_or_stay == "s":
                    clear_screen()
                    break
                elif hit_or_stay == "quit":
                    self.playing = False
                    clear_screen()
                    print(f"Thank you for playing! You're walking away with ${self.betting.bank}. Come again soon!")
                else:
                    print("Invalid entry. Try again.")

    def show_all_cards(self):
        print("Your hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:")
        for ind in range(len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")
        print("Dealer score:", self.dealer.score)

    def check_dealer_score(self):
        if self.betting.borrow_money != "n" and self.betting.borrow_money != "quit":
            self.show_all_cards()
            if self.dealer.score < 17:
                print("\nDealer takes card since score under 17.\n")
                self.dealer.add_card(self.deck.deal())
                self.check_dealer_score()
            elif self.dealer.score > 21:
                self.dealer.ace_adjust()
                if self.dealer.score > 21:
                    print(f"\nDealer busts!")
                    self.betting.winningbet()
                    self.play_again()
                else:
                    print("\nDealer Ace was adjusted from 11 points to 1 point, taking total score back under 21.")
                    self.check_dealer_score()
            else:
                self.compare_scores()
        else:
            self.goodbye()

    def compare_scores(self):
        if self.dealer.score > self.player.score:
            self.betting.losingbet()
            self.play_again()
        elif self.dealer.score == self.player.score:
            print("\nIt's a push. No one wins.")
            self.play_again()
        else: 
            self.betting.winningbet()
            self.play_again()

    def play_again(self):
        again = input("\nDo you want to play again? Y/N ").strip().lower()
        if again == "y":
            clear_screen()
            self.deck = Deck()
            self.deck.shuffle()
            self.dealer = Person()
            self.player = Person()
            self.play_game()
        elif again == "n":
            self.playing = False
            clear_screen()
            self.goodbye()
        elif again == "quit":
            self.playing = False
            clear_screen()
            self.goodbye()
        else:
            print("Invalid entry. Try again.")
            self.play_again()

    def goodbye(self):
        self.playing = False
        clear_screen()
        print(f"Thank you for playing! You\'re walking away with ${self.betting.bank} Come again soon!")

def main():
    clear_screen()
    game = Blackjack()
    game.welcome()

if __name__ == "__main__":
    main()