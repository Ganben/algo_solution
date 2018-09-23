# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/sudoku-solver/description/
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''
class Checker:
    def __init__(self):
        self.dictionary = {}
    
    def check(self, num):
        if self.dictionary.get(num) is None:
            self.dictionary[num] = True
            return True
        elif num == '.':
            return True
        else:
            return False


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        return 
        
    def find_available(self, board, row, col):
        # find a available set for row col:
        st = set([1,2,3,4,5,6,7,8,9])
        return st
        
    def boxverify(self, board):
        for i in range(0, len(board)-2, 3):
            
            for j in range(0, len(board)-2, 3):
                # 3x3 check
                checker = Checker()
                for ii in range(3):
                    for jj in range(3):
                        if not checker.check(board[i+ii][j+jj]):
                            return False

        return True
    
    def rowverify(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                # row check
                checker = Checker()
                if not checker.check(board[i][j]):
                    return False
        return True

    def colverify(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                # col check
                checker = Checker()
                if not checker.check(board[j][i]):
                    return False
        
        return True

class Test(unittest.TestCase):
    def test1(self):
        problem = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
        self.assertTrue(
            Solution().solveSudoku(problem)
        )