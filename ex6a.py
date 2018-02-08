#!/usr/bin/env python3
"""ex6.py
Author: Dalia Masilionyte
Matr.Nr.: k11726605
Exercise 6
"""

import sys
import re
import numpy as np


SEPARATOR_SIZE = 1

def createGameField(configFile):
    try:
        with open(configFile, 'r', encoding = 'utf-8') as inputFile:
            data = inputFile.read()
            width = re.search("width=([0-9].*)", data).group(1)
            width = int(width)
            height = re.search("height=([0-9].*)", data).group(1)
            height = int(height)
            p1_symbol = re.search("player1_symbol=(.*)", data).group(1)
            p1_symbol = getSymbol(p1_symbol)
            symbol_edge_length = len(p1_symbol[0])
            isValid = checkValid(symbol_edge_length, p1_symbol)
            if isValid:
                p2_symbol = re.search("player2_symbol=(.*)", data).group(1)
                p2_symbol = getSymbol(p2_symbol)
                isValid = checkValid(symbol_edge_length, p2_symbol)
                if isValid:
                    player_track_table = createTable(width, height, " ")
                    column_fill_list = [height for x in range (width)]

                    # Creating the field if the symbols are valid
                    window_width = (width * 2) + SEPARATOR_SIZE
                    window_height = height * (symbol_edge_length + SEPARATOR_SIZE)

                    board = createTable(window_width, window_height, (" " * symbol_edge_length))

                    index = 0
                    for yCoord in range(window_height):

                        index += 1

                        for xCoord in range(window_width):
                            if(xCoord % 2 == 0):
                                board[yCoord][xCoord] = "|"
                            elif index % (symbol_edge_length + SEPARATOR_SIZE) == 0:
                                board[yCoord][xCoord] = "-" * symbol_edge_length
                                index = 0


                    print(np.matrix(board))
                    print("")

        return board, p1_symbol, p2_symbol, symbol_edge_length, player_track_table, column_fill_list

    except FileNotFoundError:
        sys.exit ("Provided input file does not exist")  # Abort

def getSymbol(symbol):
    symbol = symbol.replace ('"', '')
    symbol = symbol.split (', ')
    return symbol

def checkValid(length, list):
    for i in range (len(list)):
        if len(list[i]) != length:
            return False
    return True

def createTable(width, height, element):
    table = [[element for x in range (width)] for y in range (height)]
    return table

def columnsNotFilled(column_fill_list):
    # If there are non filled columns the game is not over
    for column_index in column_fill_list:
        if column_index != 0:
            return True
    return False

def checkPlayerTrackTable(player_track_table, row, column):
    print("winner takes it all")
    for yCoord in player_track_table:
        for xCoord in player_track_table[yCoord]:



def updateGameTrackTable(player_track_table, player_no, column, row):
    player_track_table[row][column] = player_no
    print(np.matrix(player_track_table))

#### TODO GAME
def gameTurn(player_symbol, board, column, symbol_edge_length, column_fill_list, player_track_table, player_no):

    if not 0 < column <= len(column_fill_list):
        print("This column does not exist")
        turn = int(input("Enter the column:"))
        gameTurn(player_symbol, board, turn, symbol_edge_length, column_fill_list)
    else:
        # Column count starts at 0
        adjusted_column = column - 1
        row = column_fill_list[adjusted_column]
        if row == 0:
            print("This column is full")
            turn = int(input("Enter the column:"))
            gameTurn(player_symbol, board, turn, symbol_edge_length, column_fill_list)
        else:
            adjusted_row = row * (symbol_edge_length + SEPARATOR_SIZE) - symbol_edge_length - SEPARATOR_SIZE
            for symbol in player_symbol:
                board[adjusted_row][column * 2 - SEPARATOR_SIZE] = symbol
                adjusted_row += 1

            column_fill_list[adjusted_column] -= 1
            print(np.matrix(board))
            print("")

            updateGameTrackTable(player_track_table, player_no, adjusted_column, row - 1)





board, player1_symbol, player2_symbol, symbol_edge_length, \
player_track_table, column_fill_list = createGameField('configs.txt')

game_continues = True
while(game_continues):
    player1_turn = int(input("Player 1 enter the column: "))
    gameTurn(player1_symbol, board, player1_turn,
             symbol_edge_length, column_fill_list, player_track_table, "1")

    player2_turn = int(input("Player 2 enter the column: "))
    gameTurn(player2_symbol, board, player2_turn,
             symbol_edge_length, column_fill_list, player_track_table, "2")


