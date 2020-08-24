# Session 6 - First Class Functions

#### Objective of Assignment:

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 150 pts

Basics (applicable to 2/3 above):

1. Proper readme file - 50 (if not there then 0)
2. Docstrings must, and it must mention what the function is doing (2, 3) - 50
3. Write annotations for 3 - 50 pts
4. Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
5. Submit Github link with all test files and github actions in place. 

#### The github repository contains the below python files

    1. session6.py          -   file containing the code
    2. test_session.py      -   file containing the test cases

#### session6.py contains the below functions

    1. poker_set(val, suit):
    '''
    Function creates 52 cards in a deck
    '''
    
    2. check_flush(player_suits:'Player hand') -> bool:
    '''
    Function to check if a given player hand is flush or not
    Accepts player hand as input and provides boolean as output
    '''
    
    3. check_three_of_a_kind(hand:'Player_hand') -> bool:
    '''
    Function to check if a given player hand is a three of a kind
    '''
    
    4. check_four_of_a_kind(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand is a four of a kind
    '''
    
    5. check_full_house(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has a full house - basically if one pair and one
    three of a kind together 
    '''
    
    6. check_two_pairs(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has two pairs 
    '''
    
    7. check_one_pair(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has a pair
    '''
    
    8. check_straight(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a straight
    '''
    
    9. check_straight_flush(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a straight flush
    '''
    
    10. check_royal_flush(hand:'Player Hand') -> bool:
    '''
    Function to check if a given player hand has is a royal flush
    '''
    11. poker_set(val, suit):
    '''
    Function creates 52 cards in a deck
    '''
    
    12. check_hand(player: 'Player Hand') -> int:
    '''
    Function to return the rank or order in which a player is decided
    10 is of highest value and 1 is of least
    '''
    
    13. poker_winner(*, player1=None, player2=None):
    '''
    Function to decide who the winner is!!!
    '''
    
#### test_session6.py file contains test cases for the session_6.py file


    1. test_deck_using_lamda_expression():
    """
    Test case to check the creation of cards using the lambda, zip and map expression
    `deck_using_deck_expression`.
    """
    
    2. test_deck_using_normal():
    """
    Test case to check the creation of cards by normal method using loops
    `deck_using_normal_way`. Validates using the manually created cards list.
    """
    
    3. test_three_flush_3():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 3 cards
    '''
    
    4. test_three_flush_4():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 4 card hands
    '''
    
    5. test_three_flush_5():
    '''
    Test case to check the winner between player with a three of a kind or a flush for 5 card hands
    '''
    
    6. test_high_one_pair():
    '''
    Test case to check the winner between player with a high card and one pair
    '''
    
    7. test_one_two_pair_4():
    '''
    Test case to check the winner between player with a two pairs and one pair for 4 card hand
    '''
    
    8. 