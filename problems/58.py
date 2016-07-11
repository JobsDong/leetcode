#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = None

        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ':
                if start is not None:
                    return start-i
            else:
                if start is None:
                    start = i
        else:
            if start is None:
                return 0
            else:
                return start+1


if __name__ == "__main__":
    print Solution().lengthOfLastWord("Hello World")
    print Solution().lengthOfLastWord("      ")
    print Solution().lengthOfLastWord("Hello World  ")
