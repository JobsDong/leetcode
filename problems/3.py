#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        s_s = dict()

        for i, c in enumerate(s):
            if c not in s_s:
                s_s[c] = i
                length = length if length > len(s_s) else len(s_s)
            else:
                need_remove = s_s[c]
                for k, v in s_s.items():
                    if v <= need_remove:
                        del s_s[k]
                s_s[c] = i

        return length


if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("dvdf")