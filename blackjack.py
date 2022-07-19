'''
BlackJack card game
'''

from random import shuffle

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'This card is the {self.rank} of {self.suit}'
    
class Deck():
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    ranks = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
    'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    values = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5,
    'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
    'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):
        self.deck = self.shuffle_deck(self.create_deck())
    
    def create_deck(self):
        all_cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                all_cards.append(Card(suit, rank))
        return all_cards

    def shuffle_deck(self, deck):
        return shuffle(deck)

    def __len__(self):
        return len(self.deck)
    
    def __str__(self):
        return f'Cards in deck: {self.deck}'

class Player():
    #create 2 instances, user and dealer
    def __init__(self, name, type):
        self.name = name
        self.type = type #user or dealer

    def __len__(self):
        #return len(player_cards)
        pass

def game():
    pass

if __name__ == '__main__':
    game()