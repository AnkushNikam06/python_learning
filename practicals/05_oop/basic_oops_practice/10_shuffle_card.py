# To shuffle the deck of cards we need to use the shuffle module.
# Import the required module
# Declare a class named Cards which will have variables suites and values, now instead of using self.suites and self.values, we are going to declare them as global variables.
# Declare a class Deck that will have an empty list named mycardset, and the suites and values will be appended to mycardset  list.
# Declare a class ShuffleCards along with a method named shuffle() that would check the number of cards and then shuffles them.
# To remove some cards we will create a popCard() method in ShuffleCards class.

# from random import shuffle

import random

class Cards:
    global suites
    global values
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Deck:
    def __init__(self):
        self.mycardset = []
        for suit in suites:
            for value in values:
                self.mycardset.append(f"{value} of {suit}")

class ShuffleCards(Deck):
    def shuffle(self):
        if len(self.mycardset) == 52:
            random.shuffle(self.mycardset)
            print("Cards have been shuffled.")
        else:
            print("Incomplete deck! Cannot shuffle.")

    def popCard(self):
        if len(self.mycardset) > 0:
            removed_card = self.mycardset.pop()
            print(f"Card removed: {removed_card}")
            return removed_card
        else:
            print("No cards left to remove.")
            return None
        
if __name__ == "__main__":
    Cards()  
    deck = ShuffleCards()
    deck.shuffle()
    deck.popCard()
    deck.popCard()
