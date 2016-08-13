#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for c in s:
            if c in ['a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E']:
                vowels.append(c)

        new_s = []
        j = len(vowels)-1
        for i in xrange(0, len(s)):
            if s[i] in ['a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E']:
                new_s.append(vowels[j])
                j -= 1
            else:
                new_s.append(s[i])
        return "".join(new_s)

if __name__ == "__main__":
    print Solution().reverseVowels("hello")