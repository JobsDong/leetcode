#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
            return False

        l = []

        for i in xrange(0, len(s)):
            for word in wordDict:
                n = len(word)
                if n == i+1 and s[i-n+1:i+1] == word:
                    l.append(True)
                    break
                elif n < i+1 and l[i-n] and s[i-n+1:i+1] == word:
                    l.append(True)
                    break
            else:
                l.append(False)

        return l[-1]


if __name__ == "__main__":
    print Solution().wordBreak("leetcode", set(["leet", "code"]))