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

        for i, num in enumerate(nums):

            # 1
            while len(deque) > 0:
                if nums[deque[-1]] <= nums[i]:
                    deque.pop()
                else:
                    break
            # 2
            deque.append(i)
            if i - deque[0] >= k:
                deque.popleft()

            # 3
            if i >= k-1:
                results.append(nums[deque[0]])


        return results


if __name__ == "__main__":
    print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    # print Solution().maxSlidingWindow([7, 2, 4], 2)
    # print Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)