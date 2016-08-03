#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        d = dict()
        for i, c in enumerate(s):
            if c not in d:
                l.append(-1)
            else:
                l.append(d[c])
            d[c] = i

        max_len = 0
        start = -1
        for j, x in enumerate(l):
            if l[j] == -1:
                if j-start > max_len:
                    max_len += 1
            else:
                if (j-l[j]) > max_len and (j-start) > max_len:
                    max_len += 1

                if l[j] > start:
                    start = l[j]

        return max_len

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abba")
