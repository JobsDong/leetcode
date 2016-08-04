#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_num = len(board)
        col_num = len(board[0])

        for i in xrange(0, row_num):
            num_set = set()
            for j in xrange(0, col_num):
                if board[i][j] == '.':
                    pass
                else:
                    if board[i][j] in num_set or int(board[i][j]) < 1 or int(board[i][j]) > 9:
                        return False
                    else:
                        num_set.add(board[i][j])
            if len(num_set) > 9:
                return False

        for j in xrange(0, col_num):
            num_set = set()
            for i in xrange(0, row_num):
                if board[i][j] == '.':
                    pass
                else:
                    if board[i][j] in num_set or int(board[i][j]) < 1 or int(board[i][j]) > 9:
                        return False
                    else:
                        num_set.add(board[i][j])
            if len(num_set) > 9:
                return False

        for i in xrange(0, row_num-2, 3):
            for j in xrange(0, col_num-2, 3):
                num_set = set()
                for m in xrange(i, i+3):
                    for n in xrange(j, j+3):
                        if board[m][n] == '.':
                            pass
                        else:
                            if board[m][n] in num_set or int(board[m][n]) < 1 or int(board[m][n]) > 9:
                                return False
                            else:
                                num_set.add(board[m][n])
                if len(num_set) > 9:
                    return False

        return True

if __name__ == "__main__":
    print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])

