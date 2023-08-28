# Andrew Torres CIS 261 

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return None
    
    def count_cards(self):
        return len(self.deck)

deck = Deck()

deck.shuffle()

for _ in range(5):
    card = deck.deal()
    if card:
        print(f"Dealt: {card}")
    else:
        print("No more cards in the deck.")

# Print the number of cards remaining in the deck
print(f"Remaining cards in the deck: {deck.count_cards()}")

