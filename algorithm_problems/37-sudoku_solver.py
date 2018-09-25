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
        i = 0
        j = 0
        ans = board.copy()
        potentials = []
        pos = 0
        while self.is_completed(ans) is not True:
            i, j = self.is_completed(ans)
            pot = []
            valids = self.find_available(ans, i, j)
            if len(valids) > 0:
                pot.append(i)
                pot.append(j)
                ans[i][j] == valids[0]
                valids.pop(0)
                pot.append(valids)
                potentials.append(pot)
            else:
                for ii in range(potentials):
                    vvs = potentials[len(potentials) - ii]
                    if len(vvs) > 2:
                        i = vvs[0]
                        j = vvs[1]
                        ans[i][j] == vvs.pop(2)
                    else:
                        continue
                    
        return 

    def is_completed(self, board):
        #
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return True
    
    def find_available(self, board, row, col):
        # find a available set for row col:
        st = set([1,2,3,4,5,6,7,8,9])
        bi = row - (row % 3)
        bj = col = (col % 3)

        # box remove:
        for ii in range(3):
            for jj in range(3):
                if board[bi+ii][bj+jj] == '.':
                    continue
                elif int(board[bi+ii][bj+jj]) in st:
                    st.remove(int(board[bi+ii][bj+jj]))
                else:
                    continue

        # row remove:
        for i in range(9):
            if board[row][i] == '.':
                continue
            elif int(board[row][i]) in st:
                st.remove(int(board[row][i]))
            else:
                continue
        
        # col remove:
        for i in range(9):
            if board[i][col] == '.':
                continue
            elif int(board[i][col]) in st:
                st.remove(int(board[i][col]))
            else:
                continue
        
        return list(st)
        
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