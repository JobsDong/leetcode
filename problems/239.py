#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import collections

class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        deque = collections.deque()
        results = []

        max_num = None
        for i, num in enumerate(nums):
            deque.append(num)

            if i <= k-1:
                max_num = num if max_num is None or num >= max_num else max_num
            else:
                pop_left = deque.popleft()
                if num >= max_num:
                    max_num = num
                elif pop_left < max_num:
                    pass
                else:
                    max_num = max(deque)

            if i >= k-1:
                results.append(max_num)

        return results


if __name__ == "__main__":
    print Solution().maxSlidingWindow([-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], 7)