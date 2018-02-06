#!/usr/bin/env python3
"""ex6.py
Author: Dalia Masilionyte
Matr.Nr.: k11726605
Exercise 6
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
                    # Creating the field if the symbols are valid
                    window_width = (width) * (length +1) + 1
                    window_height = height * (length + 1)


                    board = [[" " for x in range (window_width)] for y in range (window_height)]
                    for h in range(window_height):

                        for w in range(window_width):
                            if(w == 0):
                                board[h][w] = '|'
                            else:
                                if(w > length-1):
                                    if(board[h][w-length-1] == "|"):
                                        board[h][w] = "|"

                                if(h >= length):
                                    if (h == length and w != 0 and board[h][w] is not '|'):
                                        board[h][w] = "-"
                                    if(board[h-length-1][w] == '-'):
                                       board[h][w] = "-"


        print(np.matrix(board))

        k = 0
        for sym in p1_symbol:
            j = 1

            for i in range(len(sym)):
                board[k][j] = sym[i]
                j+=1
            k+=1
        print("")
        print (np.matrix (board))


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


createGameField('configs.txt')
