#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tria = []
        
        if numRows == 0:
            return tria
        elif numRows == 1:
            tria.append([1])
        elif numRows == 2:
            tria.append([1])
            tria.append([1, 1])
        else:
            tria.append([1])
            tria.append([1, 1])
            for i in xrange(2, numRows):
                row = []
                
                row.append(1)
                for j in xrange(1, i):
                    row.append(tria[i-1][j-1]+tria[i-1][j])
                row.append(1)
                
                tria.append(row)
        return tria
        
if __name__ == "__main__":
    print Solution().generate(5)