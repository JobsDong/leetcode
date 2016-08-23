#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if 6 > num:
        return 1
    elif 6 < num:
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start <= end:
            mid = (start+end)/2
            result = guess(mid)
            if result == 1:
                start = mid+1
            elif result == -1:
                end = mid-1
            else:
                return mid

        return start

if __name__ == "__main__":
    print Solution().guessNumber(10)
