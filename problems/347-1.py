#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        return heapq.nlargest(k, counter, key=lambda x:counter[x])

if __name__ == "__main__":
    print Solution().topKFrequent([1,1,1,2,2,3], 2)