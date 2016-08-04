#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        sub_strs = dict()

        for i in xrange(0, n):
            if i+10 <= n:
                sub_str = s[i:i+10]
                if sub_str not in sub_strs:
                    sub_strs[sub_str] = 1
                else:
                    sub_strs[sub_str] += 1
            else:
                break

        l = []
        for k, v in sub_strs.items():
            if v >= 2:
                l.append(k)
        return l

if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

