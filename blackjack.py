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
        '''
        Using a function to create the deck with all suits and ranks
        '''
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
        self.record = [0, 0, 0, 0] #wins, losses, busts, draws

    def hit(self, card):
        self.cards.append(card)

    def value(self):
        #function to check the value of the card
        value = 0
        for i in self.cards:
            value += i.value
        return value

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return self.name

def player_creation():
    #function to create the players and their money
    player_list = []
    while True:
        try:
            players = int(input('1 Player or 2 Player? enter 1 or 2: '))
            if players not in (1, 2):
                raise ValueError
            for i in range(1, players+1):
                name = input(f"Enter player {i}'s name: ")
                money = int(input(f"Enter player {i}'s money(must be 10000 or below, and above 0): "))
                if money > 10000 or money <= 0:
                    raise ValueError
                name = Player(name, money)
                player_list.append(name)
            break
        except:
            print('Invalid answer')
    return player_list

def bet(players):
    #function to check how much the player is betting
    for player in players:
        while True:
            try:
                player.money_bet = int(input(f"{player}'s bet: "))
                if player.money_bet > player.money or player.money_bet < 0:
                    raise ValueError
                break
            except:
                print('Enter a valid amount')

def hit(player, deck):
    player.hit(deck.deck.pop(randrange(0, len(deck))))

def checkwin(player, dealer):
    '''
    function to check who won, and adjust their record and money
    '''
    if player.value() == 21:
        if dealer.value() == 21:
            print('Draw')
            player.record[3] += 1
        elif dealer.value() > 21:
            print('Dealer busted')
            player.record[0] += 1
            player.money += player.money_bet*(3/2)
        elif dealer.value() < 21:
            print(f'{player} wins')
            player.record[0] += 1
            player.money += player.money_bet*(3/2)
    if player.value() < 21:
        if dealer.value() == 21:
            print('Dealer wins')
            player.record[1] += 1
            player.money -= player.money_bet
        elif dealer.value() > 21:
            print('Dealer busted')
            player.record[0] += 1
            player.money += player.money_bet*(3/2)
        else:
            if (21-player.value()) > (21-dealer.value()):
                print('Dealer wins')
                player.record[1] += 1
                player.money -= player.money_bet
            elif (21-player.value()) < (21-dealer.value()):
                print(f'{player} wins')
                player.record[0] += 1
                player.money += player.money_bet*(3/2)
            else:
                print('Draw')
                player.record[3] += 1
    print(f'{player} now has ${player.money}')
    print(f"{player}'s record is now {player.record}")
    player.money_bet = 0

def play_again(players):
    play = True
    while play: #play again code
        try:
            play_again = input('Would you like to play again? Y or N: ')
            if play_again not in ('Y', 'N'):
                raise ValueError
            if play_again == 'Y':
                play = False
                game(players)
            elif play_again == 'N':
                break
        except ValueError:
            print('Invalid input')

def game(players):
    '''
    Function for the main game
    '''
    dealer = Player('Dealer', Infinity)
    for player in players:
        player.cards = [] #resetting the cards and deck
    deck = Deck()
    bet(players)

    for i in range(2): #dealing the cards
        hit(dealer, deck)
        for player in players:
            hit(player, deck)
    print("Dealer's cards: ")
    print(f'{dealer.cards[0]} and Hidden Card')

    for player in players: #showing the player's cards
        print(f"{player}'s cards: ")
        for card in player.cards:
            print(card)
        print(f'value: {player.value()}')
        while True:
            try: #main function of the game, hitting or standing
                decision = input(f'does {player} hit or stand?: ')
                if decision not in ('hit', 'stand'):
                    raise ValueError
                if decision == 'stand':
                    print(f'{player} is standing at {player.value()}')
                    break
                if decision == 'hit':
                    hit(player, deck)
                    print(f'new card: {player.cards[-1]}')
                    print(f'{player} is now at {player.value()}')
                    if player.value() > 21:
                        print('Bust')
                        player.money -= player.money_bet
                        player.record[1] += 1
                        break
            except:
                print('Invalid input')

    print('Since all players have gone, the Dealer will now play')
    while dealer.value() < 17:
        hit(dealer, deck)

    for player in players:
        checkwin(player, dealer)
        if player.money == 0:
            print(f'{player} has $0, game over')
            quit()

    play_again(players)
    quit()

if __name__ == '__main__':
    players = player_creation()
    game(players)
