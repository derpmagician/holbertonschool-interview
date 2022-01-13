#!/usr/bin/python3
"""Module to solve n-queens problem"""
from sys import argv

argc = len(argv)
if argc != 2:
    print('Usage: nqueens N')
    exit(1)

for c in argv[1]:
    if ord(c) < ord('0') or ord(c) > ord('9'):
        print('N must be a number')
        exit(1)

N = int(argv[1])
if N < 4:
    print('N must be at least 4')
    exit(1)


def put_queen(queens_pos, row, col):
    for pos_pair in queens_pos:
        [r, c] = pos_pair
        if r == row or c == col or \
           abs(r - row) == abs(c - col):
            return False
    return True


# start the algorithm
def n_queens(N, queens_pos, row):
    if row == N:
        print(queens_pos)
        return

    for col in range(N):
        if put_queen(queens_pos, row, col):
            queens_pos.append([row, col])
            n_queens(N, queens_pos, row + 1)
            queens_pos.pop()

n_queens(N, [], 0)

