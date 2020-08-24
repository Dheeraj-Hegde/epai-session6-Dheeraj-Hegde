import importlib
import inspect
import os
import re

import pytest

import session6


vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

README_CONTENT_CHECK_FOR = [
    'poker_set',
    'check_flush',
    'check_three_of_a_kind',
    'check_four_of_a_kind',
    'check_full_house',
    'check_two_pairs',
    'check_one_pair',
    'check_straight',
    'check_straight_flush',
    'check_royal_flush',
    'check_hand',
    'poker_winner'
]

LAMBDA_CONTENT_CHECK_FOR = [
        'lambda',
    'zip',
    'map'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_are_defined():
    content = inspect.getsource(session6)
    AllFUNCTIONSDEFINED = True
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

def test_keyword():
    LAMBDALOOKSGOOD = True
    f = open("session6.py", "r")
    content = f.read()
    f.close()
    for c in LAMBDA_CONTENT_CHECK_FOR:
        if c not in content:
            LAMBDALOOKSGOOD = False
            pass
    assert LAMBDALOOKSGOOD == True, "You have not used 'zip', 'lambda', 'map' "

def test_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    #functions = inspect.getmembers(session6, inspect.isfunction)
    #for function in functions:
    assert session6.poker_set(vals,suits).__doc__, "Docstring not used!"


def test_annotations():
    """
    Test case to check the function typing are implemented in the function
    definition.
    """
    assert session6.poker_winner.__annotations__, "Annotations not used!"

def test_deck_using_lamda_expression():
    """
    Test case to check the creation of cards using the lambda, zip and map expression
    `deck_using_deck_expression`.
    """
    assert len(session6.l1) == 52, 'Your function is incorrect, the deck should be of 52 cards'


def test_deck_using_normal():
    """
    Test case to check the creation of cards by normal method using loops
    `deck_using_normal_way`. Validates using the manually created cards list.
    """
    assert len(session6.poker_set(vals, suits)) == 52, 'Invalid number of cards in the deck'

def test_three_flush_3():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 3 cards
    '''
    assert session6.poker_winner(player1=['4S','4D','4H'], player2=['QS','JS','10S']) == "player2", "Three of a kind is lesser than flush"

def test_three_flush_4():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 4 card hands
    '''
    assert session6.poker_winner(player1=['4S','4D','4H','8S'], player2=['QS','JS','10S','2S']) == "player2", "Three of a kind is lesser than flush"

def test_three_flush_5():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 5 card hands
    '''
    assert session6.poker_winner(player1=['4S','4D','4H','8S','AS'], player2=['QS','JS','10S','2S','AS']) == "player2", "Three of a kind is lesser than flush"

def test_high_one_pair():
    '''
    Test case to check the winner between player with a high card and one pair
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','8S','AS'], player2=['QD','JH','5D','2S','AS']) == "player1", "One pair is greater than high card"

def test_one_two_pair_4():
    '''
    Test case to check the winner between player with a two pairs and one pair for 4 card hand
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','3S'], player2=['QD','QH','5D','2S']) == "player1", "Two pair is greater than one pair cards"

def test_one_two_pair_5():
    '''
    Test case to check the winner between player with a two pairs and one pair for 5 card hand
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','3S','6D'], player2=['QD','QH','5D','2S','AS']) == "player1", "Two pair is greater than one pair cards"

def test_draw_4():
    '''
    Test case to check the draw between 2 player hands
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','3S'], player2=['5S','3D','3H','5S']) == "Draw", "Two pair is equal to two pair cards"

def test_draw_5():
    '''
    Test case to check the draw between 2 player hands for 5 cards
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','3S','AD'], player2=['5S','3D','3H','5S','QD']) == "Draw", "Two pair is equal to two pair cards"

def test_straight_flush_5():
    '''
    Test case to check the winner between player with a straight or a flush for 5 card hands
    '''
    assert session6.poker_winner(player1=['4S','5D','6H','7S','8S'], player2=['QS','JS','10S','2S','AS']) == "player2", "Flush is greater than straight"

def test_straight_flush_4():
    '''
    Test case to check the winner between player with a straight or a flush for 4 card hands
    '''
    assert session6.poker_winner(player1=['4S','5D','6H','7S'], player2=['QS','JS','10S','2S']) == "player2", "Flush is greater than straight"

def test_straight_flush_3():
    '''
    Test case to check the winner between player with a straight or a flush for 3 card hands
    '''
    assert session6.poker_winner(player1=['4S','5D','6H'], player2=['QS','JS','2S']) == "player2", "Flush is greater than straight"

def test_two_pair_three():
    '''
    Test case to check the winner between player with a two pairs and 3 of a kind
    '''
    assert session6.poker_winner(player1=['4S','3D','4H','3S','AD'], player2=['QD','QH','QD','2S','5D']) == "player2", "Two pair is lesser than 3 of a kind"

def test_straight_three():
    '''
    Test case to check the winner between player with a two pairs and 3 of a kind
    '''
    assert session6.poker_winner(player1=['8S','7D','6H','5S','4D'], player2=['QD','QH','QD','2S','5D']) == "player1", "Straight is greater than 3 of a kind"

def test_flush_full():
    '''
    Test case to check the winner between player with a flush or full house
    '''
    assert session6.poker_winner(player1=['5S','5D','6H','6S','6D'], player2=['QS','JS','2S','AS','8S']) == "player1", "Flush is lesser than full house"

def test_full_four():
    '''
    Test case to check the winner between player with a four of a kind or full house
    '''
    assert session6.poker_winner(player1=['5S','5D','6H','6S','6D'], player2=['QS','QD','QH','QC','8S']) == "player2", "Four of a kind is greater than full house"

def test_four_straightflush():
    '''
    Test case to check the winner between player with a straight flush or four of a kind
    '''
    assert session6.poker_winner(player1=['5S','6S','7S','8S','9S'], player2=['QS','QD','QH','QC','8S']) == "player1", "Four of a kind is lesser than straight flush"

def test_straight_royalflush():
    '''
    Test case to check the winner between player with a straight flush or royal flush
    '''
    assert session6.poker_winner(player1=['5S','6S','7S','8S','9S'], player2=['AS','KS','QS','JS','10S']) == "player2", "Royal Flush is greater than straight flush"
