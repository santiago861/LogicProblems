#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    longit = len(matrix) // 2
    finalMatrix = []
    sum = 0

    for line in range(0, longit):
        x = len(matrix) // 2 # this is the cuadrant we want to calculate n * n
        y = len(matrix) // 2 # this is the cuadrant we want to calculate n * n
        line = []

        for column in range(0, longit):
            if x == 1:
                if x == 1 and y == 1:
                    elemMax = max(matrix[line][column], matrix[line][(x*2) + 1], matrix[(y*2) + 1][column], matrix[(y*2) + 1][(x*2) + 1])
                    line.append(elemMax)
                else:
                    elemMax = max(matrix[line][column], matrix[line][(x*2) + 1], matrix[y*2][column], matrix[y*2][(x*2) + 1])
                    line.append(elemMax)
            else:
                if y == 1:
                    elemMax = max(matrix[line][column], matrix[line][x*2], matrix[(y*2) + 1][column], matrix[(y*2) + 1][x*2])
                    line.append(elemMax)
                else: 
                    elemMax = max(matrix[line][column], matrix[line][x*2], matrix[y*2][column], matrix[y*2][x*2])
                    line.append(elemMax)
            x -= 1

            
        y -= 1
        finalMatrix.append(line)
    
    for i in range(len(finalMatrix)):
        for j in range(len(finalMatrix)):
            sum += j
    return sum 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
