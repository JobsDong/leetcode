#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

from collections import deque


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return

        que = deque()

        for i in [0, m-1]:
            for j in xrange(0, n):
                if board[i][j] == 'O':
                    board[i][j] = 'S'
                    que.append((i, j))

        for j in [0, n-1]:
            for i in xrange(1, m-1):
                if board[i][j] == 'O':
                    board[i][j] = 'S'
                    que.append((i, j))

        while que:
            i, j = que.popleft()

            if i-1 >= 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'S'
                que.append((i-1, j))
            if i+1 < m and board[i+1][j] == 'O':
                board[i+1][j] = 'S'
                que.append((i+1, j))
            if j-1 >= 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'S'
                que.append((i, j-1))
            if j+1 < n and board[i][j+1] == 'O':
                board[i][j+1] = 'S'
                que.append((i, j+1))

        for i in xrange(0, m):
            for j in xrange(0, n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        print board

if __name__ == "__main__":
    Solution().solve([list('XXXX'), list('XOOX'), list('XXOX'), list('XOXX')])
    # Solution().solve([list('OO'), list('OO')])