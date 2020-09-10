# TicTacToe Game

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


# the game board
board = [[" 1 |", " 2 ", "| 3 "], [" 4 |", " 5 ", "| 6 "], [" 7 |", " 8 ", "| 9 "]]
import os

# variebles
player1 = ''  # player 1 symbol
player2 = ''  # player 2 symbol
playstate = True  # bool to stop while loop
turn_num = 0  # int to idicate which player plays
player_num = 1  # string to print the player's name
choose_place = ''  # choosing place in the board


# start functions

# checking all the winning options
def wincheck():
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    if board[1][0] == board[1][1] == board[1][2]:
        return True
    if board[2][0] == board[2][1] == board[2][2]:
        return True
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[1][2] == board[1][1] == board[2][0]:
        return True
    return False


# print the board
def boardprint():
    #  print('\n' * 100)
    os.system('cls')
    for row in board:
        row_str = ""
        for col in row:
            row_str += col
        print(row_str)


# choose where the player wants to put his symbol
def turn(player_num, board_place):
    global turn_num
    player_symbol = ''
    row = 0
    col = 0
    # which player symbol we put in the board
    if player_num == 1:
        player_symbol = player1
    elif player_num == 2:
        player_symbol = player2

    # checking all the board places options
    if board_place == 1:
        row = 0
        col = 0
    elif board_place == 2:
        row = 0
        col = 1
    elif board_place == 3:
        row = 0
        col = 2
    elif board_place == 4:
        row = 1
        col = 0
    elif board_place == 5:
        row = 1
        col = 1
    elif board_place == 6:
        row = 1
        col = 2
    elif board_place == 7:
        row = 2
        col = 0
    elif board_place == 8:
        row = 2
        col = 1
    elif board_place == 9:
        row = 2
        col = 2
        # if the board place is not empty
    if board[row][col] == " " + 'X' + " " or board[row][col] == " " + 'O' + " ":
        print("\nTHIS PLACE ALREADY HAS A SYMBOL\n")
        boardprint()
        # return the turn to the same player to try again
        turn_num -= 1
        return
    # if the place in the board is empty
    board[row][col] = " " + player_symbol + " "
    boardprint()


# who's playing with x and who's playing with o
def chooseplayer():
    global player1, player2
    while True:
        player1 = input("PLAYER 1, WOULD YOU BE X OR O : ").upper()
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            print('Your need to choose X or O')


# exit game function
def exitgame():
    input_lol = input('\nenter to quit')


# end functions


print("\nWELCOME TIC TAC TOE\n")

# CHOOSE PLAYER 1 AND PLAYER 2 SYMBOLS
chooseplayer()

# instructions
print('\nOK, BEFORE WE BEGIN THE GAME, PLAYER 1 IS {}, PLAYER 2 IS {}'.format(player1, player2))
print('\nTHE BOARD IS EMPTY:\n')
boardprint()

# player starts play
while playstate:
    turn_num += 1
    if turn_num % 2 != 0:
        player_num = 1
    else:
        player_num = 2
    choose_place = int(input(
        f'\nPlayer {player_num}, its your turn.\nEnter a place in the board you want to put your symbol in: '))
    print()
    # checking valid input from the player
    if 1 <= choose_place <= 9:
        turn(player_num, choose_place)
    else:
        print('\nenter a num between 1 to 9')
    # check if one of the player have won
    if turn_num >= 5:
        if wincheck():
            # stop the while loop
            playstate = False
            # print the winner
            print('\nplayer {} win the game!'.format(player_num))
            print('\nTHE GAME HAS ENDED')
            break
            # if the board is full and there is no winner
        elif turn_num >= 9:
            print('THE GAME HAS ENDED BOTH PLAYER FAILED TO WIN')
            break

# game ends
exitgame()
