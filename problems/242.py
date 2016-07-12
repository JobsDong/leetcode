#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        t_dict = {}
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        if len(t_dict) != len(s_dict):
            return False
        for k, v in s_dict.iteritems():
            if k not in t_dict:
                return False
            if t_dict[k] != s_dict[k]:
                return False
        return True


if __name__ == "__main__":
    print Solution().isAnagram("anagram", "nagaram")
    print Solution().isAnagram("rat", "car")