from itertools import cycle, product
import collections

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

l1 = list(map(lambda x: x, zip(vals * len(suits), suits * len(vals))))


def poker_set(val, suit):
    '''
    Function creates 52 cards in a deck
    '''
    x = list(product(val, suit))
    return x

order_of_card = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":11, "Q":12, "K":13, "A":14}

def check_flush(player_suits:'Player hand') -> bool:
    '''
    Function to check if a given player hand is flush or not
    Accepts player hand as input and provides boolean as output
    '''

    suits = [i[-1] for i in player_suits]

    if len(set(suits)) == 1:
        return True
    else:
        return False

def check_three_of_a_kind(hand:'Player_hand') -> bool:
    '''
    Function to check if a given player hand is a three of a kind
    '''
    values = [i[0] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v]+= 1
    for i in value_counts.values():
        if i == 3:
            return True

def check_four_of_a_kind(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand is a four of a kind
    '''
    values = [i[0] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v]+= 1
    for i in value_counts.values():
        if i == 4:
            return True

def check_full_house(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has a full house - basically if one pair and one
    three of a kind together
    '''
    values = [i[0] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v]+= 1
    if sorted(value_counts.values()) == [2,3]:
        return True

def check_two_pairs(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has two pairs
    '''
    values = [i[:-1] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v]+= 1
    if len(values) == 5:
        if sorted(value_counts.values()) == [1,2,2]:
            return True
    elif len(values) == 4:
        if sorted(value_counts.values()) == [2, 2]:
            return True

def check_one_pair(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has a pair
    '''
    values = [i[:-1] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v]+= 1
    if 2 in value_counts.values():
        return True

def check_straight(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a straight
    '''
    values = [i[:-1] for i in hand]
    value_counts = collections.defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [order_of_card[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else:
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True

def check_straight_flush(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a straight flush
    '''
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_royal_flush(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a royal flush
    '''
    if check_straight_flush(hand):
        values = [i[:-1] for i in hand]
        if values == ['A','K','Q','J','10']:
            return True
        else:
            return False

def check_hand(player: 'Player Hand') -> int:
    '''
    Function to return the rank or order in which a player is decided
    10 is of highest value and 1 is of least
    '''
    if check_royal_flush(player):
        print("Royal")
        return 10
    elif check_straight_flush(player):
        print("Straight")
        return 9
    elif check_four_of_a_kind(player):
        print("Four")
        return 8
    elif check_full_house(player):
        print("Full")
        return 7
    elif check_flush(player):
        print("Flush")
        return 6
    elif check_straight(player):
        print("Straight")
        return 5
    elif check_three_of_a_kind(player):
        print("Three")
        return 4
    elif check_two_pairs(player):
        print("Two Pairs")
        return 3
    elif check_one_pair(player):
        print("One Pair")
        return 2
    else:
        print("High Card")
        return 1

def poker_winner(player1:'Player 1 hand', player2: 'Player 2 hand') ->str:
    '''
    Function to decide who the winner is!!!
    '''
    if None:
        pass
    elif check_hand(player1) > check_hand(player2):
        print("player1 wins")
        return "player1"
    elif check_hand(player1) == check_hand(player2):
        return "Draw"
    else:
        print("player2 wins")
        return "player2"

#check_one_pair(['3H','3H','5S','5H'])

check_two_pairs(['3H','3H','5S','5H'])

#check_full_house(['3H','3H','5S','5H'])

#check_four_of_a_kind(['3H','3H','5S','5H'])

#check_three_of_a_kind(['3H','3H','5H','5S'])

#poker_winner(player1=['3H', '10H', 'AH'], player2=['7S', '8S', '9S'])

#check_straight(['3H','4H','5H','6S','7H'])

#check_straight_flush(['2H','3H','4H','5H','6H'])

#check_royal_flush(['AH','KH','QH','JH','10H'])


##poker_winner(player1=['4S','4D','4H'], player2=['QS','JS','10S'])
poker_winner(player1=['4S','3D','4H','3S'], player2=['QD','AH','5D','2S'])
