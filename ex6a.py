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
                    playerTrackTable = createTable(width, height, " ")
                    columnFillList = [height for x in range (width)]

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

        return board, p1_symbol, p2_symbol, symbol_edge_length, playerTrackTable, columnFillList

    except FileNotFoundError:
        sys.exit ("Provided input file does not exist")  # Abort

def getSymbol(symbol):
    symbol = symbol.replace ('"', '')
    symbol = symbol.split (', ')
    return symbol


def checkValid(length, list):
    valid = True
    for i in range (len(list)):
        if (len(list[i]) != length):
            valid = False
    return valid

def createTable(width, height, element):
    table = [[element for x in range (width)] for y in range (height)]
    return table


# def checkColumn(column, boardWidth, boardHeight):
#     # valid = False
    # if(column < 0 or column > boardWidth):
    #     valid = False
    # elif(column != 1):
    #     column * 2 - 1
    #     if(column > boardWidth):
    #         valid = False
    #     else:
    #         valid = True
    #
    # return valid

# def isFull(column, symbol_edge_length):
#     if(column in fillBoard):
#         if (fillBoard[column] == symbol_edge_length):
#             isFull = True
#     else:
#         isFull = False
#     return isFull



#### TODO GAME
def gameTurn(playerSymbol, board, column, symbol_edge_length, columnFillList):
    # if (checkColumn(column, board.shape[1], symbol_edge_length) == False):
    #     print("Invalid turn")
    #     return
    # print(np.matrix(board))
    # print("")
    row = columnFillList[column-1]
    if row == 0:
        print("This column is full")
        turn = int(input("Enter the column:"))
        gameTurn(playerSymbol, board, turn, symbol_edge_length, columnFillList)
    else:
        adjusted_row = row * (symbol_edge_length + SEPARATOR_SIZE) - symbol_edge_length - SEPARATOR_SIZE
        for symbol in playerSymbol:
            board[adjusted_row][column * 2 - SEPARATOR_SIZE] = symbol
            adjusted_row += 1

        columnFillList[column-1] -= 1
        print(np.matrix(board))




board, p1, p2, symbol_edge_length, playerTrackTable, columnFillList = createGameField('configs.txt')

while(True):
    player1_turn = int(input("Player 1 enter the column: "))
    gameTurn (p1, board, player1_turn, symbol_edge_length, columnFillList)
    player2_turn = int(input("Player 2 enter the column: "))
    gameTurn (p2, board, player2_turn, symbol_edge_length, columnFillList)


