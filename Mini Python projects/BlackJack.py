# BackJack Game

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Class for Cards, stores suit and rank

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # print the card
        return self.rank + " of " + self.suit


# class for the player hand


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)  # adding card to the card's list
        if card.rank == "Ace":  # checking for aces
            self.aces += 1
            self.adjust_for_ace()
        else:
            self.value += values[card.rank]  # adding the value of the card to the total hand value
        #  print(f"\nNEW Card: {card}, HAND Value: {self.value}, HAND Aces: {self.aces}")

    def adjust_for_ace(self):  # adjust ace value to the hand's value
        if self.value <= 10:
            self.value += 11
        else:
            self.value += 1

    def __str__(self):  # print cards, value, aces
        str = ''
        for card in self.cards:
            str += f'\n{card.rank} OF {card.suit}'
        #  str += f'\nValue N.  : {self.value} '
        #  str += f'\nAces N.  : {self.aces} '
        return str


# Class for Deck, stores in the list all 52 cards


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # adding card to the deck
        self.shuffle()  # shuffle the deck

    # print the deck

    def __str__(self):  # print the deck
        str = "\n52 Deck Cards: \n\n"
        for card in self.deck:
            str += card.rank + " of " + card.suit + " , \n"
        return str

    # shuffle the deck

    def shuffle(self):  # shuffle function from import random
        random.shuffle(self.deck)

    # dealing out a card from Deck TO Hand

    def deal(self, hand: Hand):
        deal_card = self.deck.pop()  # popping out card from the deck
        hand.add_card(deal_card)  # adding card to the hand

    def print_deck(self):
        pass


# class for bets at the beginning of the game


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        while True:
            try:
                bet = int(input("\nPlease enter a bet: "))
                if self.total >= bet > 0:
                    self.bet = bet
                    print(f'\nYOUR TOTAL CHIPS: {self.total}')
                    print(f'\nYOUR BET : {self.bet}')
                    break
                else:
                    print(
                        f"\nbet is greater than your total Chips, OR you entered a ZERO/MINUS.  \nPlease enter another bet, lower or equal to {self.total}")
            except:
                print("\nOops, you did not enter an integer!")


# Function Definitions
# This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17

def hit(deck: Deck, hand: Hand):  # deal one card off the deck and add it to the hand
    deck.deal(hand)


def hit_or_stand(deck: Deck, hand: Hand):
    global playing  # to control an upcoming while loop
    while True:
        str = input("\nFOR HIT ENTER ' -1- ' , FOR STAND ENTER ' -2- ' ")
        if str == '1':  # player hits
            hit(deck, hand)
            break
        elif str == '2':  # player stand
            playing = False
            break
        else:
            print('\nPLEASE ENTER -1- OR -2- ')


# shows the dealer and player cards except first dealer card

def show_some(player: Hand, dealer: Hand):
    print('\nSHOW SOME')
    print('\nPlayer\'S HAND: ')
    print(player)  # printing the player's hand
    print(f'\nValue N.  : {player.value}')
    print('\nDealer\'S HAND: ')
    str = ''
    for card in dealer.cards:
        if card == dealer.cards[0]:
            str += '- HIDDEN - '  # first card is hidden from the player
        else:
            str += f'\n{card.rank} OF {card.suit}'
    #  str += f'\nValue N.  : {dealer.value} '
    #  str += f'\nAces N.  : {dealer.aces} '
    print(str)  # printing the dealer's hand without the first card


# shows all of the dealer and the player cards

def show_all(player: Hand, dealer: Hand):
    print('\nSHOW ALL')
    print('\nPlayer\'S HAND: ')
    print(player)  # printing player's hand
    print(f'\nValue N.  : {player.value}')
    print('\nDealer\'S HAND: ')
    print(dealer)  # printing dealer's hand
    print(f'\nValue N.  : {dealer.value}')


#  player busts scenario - print lose massage, lost bet, stop playing

def player_busts(chip: Chips):
    global playing
    playing = False
    chip.lose_bet()
    print('\nPLAYER BUSTS! PLAY BETTER NEXT TIME')
    print(f'\nYour total chips: {chip.total}')


# player win scenario - print win massage, win bet, stop playing

def player_win(chip: Chips):
    global playing
    playing = False
    chip.win_bet()
    print('\nPLAYER WIN THE GAME! WELL DONE!')
    print(f'\n your total chips: {chip.total}')


#  dealer busts scenario - player wins - print win massage, win bet, stop playing

def dealer_busts(chip: Chips):
    global playing
    playing = False
    chip.win_bet()
    print('\nDEALER BUSTS, PLAYER WIN THE GAME! WELL DONE!')
    print(f'\n your total chips: {chip.total}')


#  dealer wins scenario - player lose - print lose massage, lose bet, stop playing

def dealer_wins(chip: Chips):
    global playing
    playing = False
    chip.lose_bet()
    print('\nDEALER WIN, PLAYER LOSE THE GAME! PLAY BETTER NEXT TIME')
    print(f'\nYour total chips: {chip.total}')


#  none player to dealer wins
def push():
    print("\nDealer and Player tie! It's a push.")


def test():
    my_card1 = Card("Hearts", "Ace")
    my_card2 = Card("Hearts", "Ace")
    my_card3 = Card("Hearts", "Ace")
    my_hand = Hand()
    my_hand.add_card(my_card1)
    my_hand.add_card(my_card2)
    my_hand.add_card(my_card3)
    print(my_hand)
    my_deck = Deck()
    print(my_deck)
    hit(my_deck, my_hand)
    print(my_hand)
    print('\n----------')
    print('----------')
    print('----------')
    show_all(my_hand, my_hand)
    print('\n----------')
    print('----------')
    print('----------')
    show_some(my_hand, my_hand)


while True:

    # Print an opening statement

    print('\nWELCOME TO BLACKJACK!')

    # Create & shuffle the deck, deal two cards to each player

    game_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    hit(game_deck, player_hand)
    hit(game_deck, player_hand)
    hit(game_deck, dealer_hand)
    hit(game_deck, dealer_hand)

    # Set up the Player's chips

    game_chips = Chips()
    game_chips.take_bet()

    # Show cards (but keep one dealer card hidden)

    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand

        hit_or_stand(game_deck, player_hand)

        # Show cards (but keep one dealer card hidden)

        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        if player_hand.value > 21:
            player_busts(game_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        while dealer_hand.value < 17:
            hit(game_deck, dealer_hand)

        # Show all cards

        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        # Inform Player of their chips total

        if dealer_hand.value > 21:
            dealer_busts(game_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(game_chips)
        elif player_hand.value > dealer_hand.value:
            player_win(game_chips)
        else:
            push()

        # Ask to play again
        play = input("\nIF YOU WANT TO PLAY AGAIN ENTER ' Y ' , IF NOT ENTER ' N '").capitalize()
        if play == 'Y':
            playing = True
            break
        else:
            print('\nTHANKS FOR PLAYING')
            break

    if not playing:
        break