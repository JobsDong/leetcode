#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1


        l = heapq.nlargest(k, [(value, key) for key, value in d.items()])
        return [i[1] for i in l]


if __name__ == "__main__":
    print Solution().topKFrequent([1,1,1,2,2,3], 2)