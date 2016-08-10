#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_citations = sorted(citations, reverse=True)
        n = len(sorted_citations)
        i = n-1

        h = 0
        while i >= 0:
            if i+1 >= sorted_citations[i]:
                h = h if h > sorted_citations[i] else sorted_citations[i]
            else:
                h = h if h > i+1 else i+1

            i -= 1

        return h

if __name__ == "__main__":
    print Solution().hIndex([4, 4, 0 ,0])