'''
BlackJack card game that utilizes OOP
'''
from random import shuffle, randrange
from numpy import Infinity

class Card():
    '''
    Created a class for each card
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Deck.values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

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
        return f'{len(self.deck)} cards in the deck'

class Player():
    '''
    Created a class for the players
    '''
    def __init__(self, name, money):
        self.name = name
        self.cards = []
        self.money_bet = 0
        self.money = money
        self.record = [0, 0, 0] #wins, losses, busts

    def hit(self, card):
        self.cards.append(card)

    def value(self):
        value = 0
        for i in self.cards:
            value += i.value
        return value

    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return self.name

#player can stand or hit
#player wins 3:2 amount of money
#keep track of player record, tell them if they bust or get 21

def player_creation():
    player_list = []
    while True:
        try:
            players = int(input('1 Player or 2 Player? enter 1 or 2: '))
            if players != 1 and players != 2:
                raise ValueError
            for i in range(1, players+1):
                name = input(f"Enter player {i}'s name: ")
                money = int(input(f"Enter player {i}'s money(must be 10000 or below): "))
                if money > 10000:
                    raise ValueError
                name = Player(name, money)
                player_list.append(name)
            break
        except: 
            print('Invalid answer')
    return player_list

def bet(players):
    for i in range(len(players)):
        while True:
            try:
                players[i].money_bet = int(input(f'How much is {players[i]} betting this round: '))
                if players[i].money_bet > players[i].money or players[i].money_bet < 0:
                    raise ValueError
                break
            except:
                print('Enter a valid amount')

def hit(player, deck):
    player.hit(deck.deck.pop(randrange(0, len(deck))))
            
def game():
    players = player_creation()
    dealer = Player('Dealer', Infinity)
    deck = Deck()
    bet(players)

    for i in range(2):
        hit(dealer, deck)
        for j in range(len(players)):
            hit(players[j], deck)
    
    for i in range(len(players)):
        print('player cards: ')
        for j in players[j].cards:
            print(j)
        print(f'value: {players[i].value()}')
        while True:
            try:
                decision = input(f'does {players[i]} hit or stand?: ')
                if decision == 'stand':
                    print(f'{players[i]} is standing at {players[i].value()}')
                elif decision == 'hit':
                    hit(players[i], deck)
                    print(f'new card: {players[i].cards[-1]}')
                    print(f'{players[i]} is now at {players[i].value()}')
                else:
                    raise ValueError
                break
            except:
                print('Invalid input')

if __name__ == '__main__':
    game()
