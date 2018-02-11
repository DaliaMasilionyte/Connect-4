#!/usr/bin/env python3
"""ex5.py
Author: Dalia Masilionyte
Matr.Nr.: k11726605
Exercise 5
"""

import sys
import re
import numpy as np

SEPARATOR_SIZE = 1


# Function to create the game field

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

        return board, p1_symbol, p2_symbol, symbol_edge_length, player_track_table, column_fill_list

    except FileNotFoundError:
        sys.exit ("Provided input file does not exist")  # Abort

# Function to format symbol
def getSymbol(symbol):
    symbol = symbol.replace ('"', '')
    symbol = symbol.split (', ')
    return symbol

# Function to check symbol validity
def checkValid(length, list):
    for i in range (len(list)):
        if len(list[i]) != length:
            return False
    return True

# Function for creating matrices
def createTable(width, height, element):
    table = [[element for x in range (width)] for y in range (height)]
    return table

board, player1_symbol, player2_symbol, symbol_edge_length, \
player_track_table, column_fill_list = createGameField('configs.txt')

print(np.matrix(board))