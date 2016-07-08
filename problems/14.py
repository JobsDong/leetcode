#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ""
        i = 0
        long_prefix = ""

        while i < len(strs[0]):
            c = strs[0][i]
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return long_prefix
            long_prefix += c
            i += 1
        return long_prefix


if __name__ == "__main__":
    print Solution().longestCommonPrefix([])