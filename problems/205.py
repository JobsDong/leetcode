#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_d = dict()
        t_d = dict()

        i = 0
        while i < len(s):
            if s[i] in s_d:
                if s_d[s[i]] != t[i]:
                    return False
            else:
                s_d[s[i]] = t[i]

            if t[i] in t_d:
                if t_d[t[i]] != s[i]:
                    return False
            else:
                t_d[t[i]] = s[i]
            i += 1

        return True


if __name__ == "__main__":
    print Solution().isIsomorphic("egg", "add")
    print Solution().isIsomorphic("foo", "bar")
    print Solution().isIsomorphic("paper", "title")
    print Solution().isIsomorphic("ab", "aa")