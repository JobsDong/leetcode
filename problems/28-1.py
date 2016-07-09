#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        i = 0
        count = 0

        while True:

            print "+++", i

            j = 0
            while True:
                if j == m:
                    print "--", count
                    return i
                if i + j == n:
                    print "---", count
                    return -1
                if haystack[i+j] != needle[j]:
                    break
                j += 1

            count += j

            i += 1



if __name__ == "__main__":
    print Solution().strStr("babbbbbabb", "bbab")
    # print Solution().strStr("abcdefabas", "def")