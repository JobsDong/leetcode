#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    
    def c(self, i, j):
        total = 1
        divide = 1
        for k in xrange(0, j):
            total *= i-k
        for k in xrange(j, 0, -1):
            divide *= k
        return total / divide
        
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        array = []
        
        if n == 0:
            return [1]
        if n == 1:
            return [1, 1]
        
        for i in xrange(0, n/2+1):
            array.append(self.c(n, i))
        
        if n % 2 == 0:
            array += array[-2::-1]
        else:
            array += array[::-1]
        
        return array
        
if __name__ == '__main__':
    print Solution().getRow(4)
