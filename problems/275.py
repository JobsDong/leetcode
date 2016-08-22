#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']



class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0

        start = 0
        end = n-1

        while start < end:

            if start+1 == end:
                if n-end >= citations[end]:
                    h = citations[end]
                else:
                    h = n-end

                if n-start >= citations[start]:
                    if citations[start] > h:
                        h = citations[start]
                else:
                    if n-start > h:
                        h = n-start

                return h

            mid = (start+end)/2

            if n-mid >= citations[mid]:
                start = mid
            else:
                end = mid

        return citations[start] if n-start >= citations[start] else n-start

if __name__ == '__main__':
    print Solution().hIndex([100])