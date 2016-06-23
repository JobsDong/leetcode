#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []

        for num in nums:
            heapq.heappush(h, (-num, num))

        for i in xrange(0, k-1):
            heapq.heappop(h)

        return heapq.heappop(h)[1]

if __name__ == "__main__":
    print Solution().findKthLargest([3,2,1,5,6,4], 2)