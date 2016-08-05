#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")

        if len(words) != len(pattern):
            return False

        p_d = dict()
        w_d = dict()

        i = 0
        while i < len(pattern):
            if pattern[i] in p_d:
                if p_d[pattern[i]] != words[i]:
                    return False
                else:
                    p_d[pattern[i]] = words[i]
            else:
                p_d[pattern[i]] = words[i]

            if words[i] in w_d:
                if w_d[words[i]] != pattern[i]:
                    return False
                else:
                    w_d[words[i]] = pattern[i]
            else:
                w_d[words[i]] = pattern[i]

            i += 1

        return True

if __name__ == "__main__":
    print Solution().wordPattern("jquery", "jquery")