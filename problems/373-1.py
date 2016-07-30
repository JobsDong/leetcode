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
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        result = []
        queue = []

        i = 0
        while i < len(nums1) + len(nums2):
            j = min(i, len(nums1)-1)

            while j >= 0 and 0 <= i-j < len(nums2):
                heapq.heappush(queue, (nums1[j] + nums2[i-j], nums1[j], nums2[i-j]))
                j -= 1

            r = heapq.heappop(queue)
            result.append([r[1], r[2]])
            if len(result) >= k:
                return result

            i += 1

        while len(result) < k and len(queue) > 0:
            r = heapq.heappop(queue)
            result.append([r[1], r[2]])

        return result


if __name__ == "__main__":
    print Solution().kSmallestPairs([], [3, 5, 7, 9], 1)