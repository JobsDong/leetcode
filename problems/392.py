#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(t)

        j = 0

        for c in s:

            while j < n and t[j] != c:
                j += 1

            if j == n:
                return False
            else:
                j += 1

        return True

if __name__ == "__main__":
    print Solution().isSubsequence("abc", "ahbgdc")
    print Solution().isSubsequence("axc", "ahbgdc")
