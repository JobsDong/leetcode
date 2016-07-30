#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        l = []

        for i in nums1[:k]:
            for j in nums2[:k]:
                heapq.heappush(l, (-(i+j), (i, j)))
                if len(l) > k:
                    heapq.heappop(l)

        result = []
        while len(l) > 0:
            result.append(heapq.heappop(l)[1])
        return result[-1::-1]


if __name__ == "__main__":
    print Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)