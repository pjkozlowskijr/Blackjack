def bet(self):
        input = input("Would you like to bet? Please respond with 'yes' or 'no' ")
        if input.lower() =='yes':
            amount = input(int(f"Now its interesting, how much would you like to bet? You currently have: ${self.bank} "))
            self.bank -= amount
            print (f"This is where the fun begins, lets see what will be come of the ${amount} you have risked")
        elif input.lower()=='no':
            print('Well thats not any fun, why come to a BlackJack table if you wont risk anything?')
        else:
            print('Invalid response, please try again')
