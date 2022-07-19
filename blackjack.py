'''
BlackJack card game
'''
from random import shuffle

class Card():
    '''
    Created a class for each card
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'This card is the {self.rank} of {self.suit}'

class Deck():
    '''
    Created a class for the deck
    '''
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    ranks = ['Two', 'Three', 'Four', 'Five', 'Six',
    'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5,
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
        shuffle(deck)
        return deck

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        printable_deck = [f'{x} of {y}' for y in Deck.suits for x in Deck.ranks] #y is outer loop
        return f'Cards in deck: {printable_deck}'

class Player():
    '''
    Created a class for the players
    '''
    def __init__(self, name, type, cards, money):
        self.name = name
        self.type = type #user or dealer
        self.cards = cards
        self.money = money
        self.record = [0, 0, 0] #wins, losses, busts

    def hit(self, card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

#player can stand or hit
#pick betting amount
#player wins 3:2 amount of money
#keep track of player record, tell them if they bust or get 21
#add multiple players
#double down doubles bet, and player only receives one card
#can only double down after dealt first 2 cards

def game():
    #all that's left is game logic
    money_bet = 0
    player_list = []

if __name__ == '__main__':
    game()
