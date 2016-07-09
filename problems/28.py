#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def next_cache(self, needle):
        cache = [0]

        for i in xrange(1, len(needle)):
            if needle[i] == needle[cache[i-1]]:
                cache.append(cache[i-1] + 1)
            else:
                cache.append(0)

        return cache

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        next_cache = self.next_cache(needle)

        i = 0
        j = 0
        while True:

            while True:
                if j == m:
                    return i
                if j + i == n:
                    return -1
                if haystack[i+j] != needle[j]:
                    if j == 0:
                        i += 1
                        j = 0
                    else:
                        i = i + j - next_cache[j-1]
                        j = next_cache[j-1]
                    break
                j += 1


if __name__ == "__main__":
    # print Solution().next_cache2("ABCDABCE")
    # print Solution().next_cache("ABCDABCE")
    # print Solution().next_cache("abab")
    print Solution().strStr("babbbbbabb", "bbab")
    print Solution().strStr("", "")