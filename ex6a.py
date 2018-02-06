#!/usr/bin/env python3
"""ex5.py
Author: Dalia Masilionyte
Matr.Nr.: k11726605
Exercise 5
"""

import sys
import re
import numpy as np


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
            length = len(p1_symbol[0])
            isValid = checkValid(length, p1_symbol)
            if isValid:
                p2_symbol = re.search("player2_symbol=(.*)", data).group(1)
                p2_symbol = getSymbol(p2_symbol)
                isValid = checkValid(length, p2_symbol)
                if isValid:
                    playerTrackTable = createTable(width, height)
                    columnFillList = [height for x in range (width)]

                    # Creating the field if the symbols are valid
                    window_width = (width * 2)  + 1
                    window_height = height * (length + 1)

                    board = [[(" " * length) for x in range (window_width)] for y in range (window_height)]

                    for h in range(window_height):
                        for w in range(window_width):
                            if(w == 0):
                                board[h][w] = '|'
                            else:
                                if(w % 2 == 0):
                                    board[h][w] = "|"
                                if(h % length == 0):
                                    if (board[h][w] is not '|'):
                                        board[h][w] = "-" * length
                                    # if(board[h-length-1][w] == '-'):
                                    #    board[h][w] = "-" * length


                    print(np.matrix(board))



                    print("")

                    # k = 0
                    # j = 1
                    # for symbol in p1_symbol:
                    #     board[k][j] = symbol
                    #     k+=1
                    # print(np.matrix (board))
        return board, p1_symbol, p2_symbol, length, playerTrackTable, columnFillList

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

def createTable(width, height):
    table = [[" " for x in range (width)] for y in range (height)]
    return table


def checkColumn(column, boardWidth, boardHeight):
    valid = False
    if(column < 0 or column > boardWidth):
        valid = False
    elif(column != 1):
        column * 2 - 1
        if(column > boardWidth):
            valid = False
        elif(isFull(column, boardHeight)):
            valid = False
        else:
            valid = True

    return valid

def isFull(column, boardHeight):
    if(column in fillBoard):
        if (fillBoard[column] == boardHeight):
            isFull = True
    else:
        isFull = False
    return isFull


#### TODO GAME
def gameTurn(player, board, column, boardHeight):
    valid = checkColumn(column, board.shape[1], boardHeight)
    if (valid == False):
        print("Invalid turn")
    else:
        if column in fillBoard:

    ##### TODO implement the turn

            fillBoard[column] += 1
        else:
            fillBoard[column] = 1


board, p1, p2, boardHeight, playerTrackTable, columnFillList = createGameField('configs.txt')
fillBoard = {}
firstTurn = input("Player 1 enter the column: ")
firstTurn = int(firstTurn)
gameTurn(p1, board, firstTurn, boardHeight)
