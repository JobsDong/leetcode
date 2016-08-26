#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if t < 0:
            return False

        d = {}
        for i, num in enumerate(nums):
            if t == 0:
                m = num
            else:
                m = num/t

            if m in d:
                return True
            if m-1 in d and abs(d[m-1]-num) <= t:
                return True
            if m+1 in d and abs(d[m+1]-num) <= t:
                return True
            d[m] = num
            if i >= k:
                if t == 0:
                    del d[nums[i-k]]
                else:
                    del d[nums[i-k]/t]
        return False

if __name__ == "__main__":
    print Solution().containsNearbyAlmostDuplicate([-1, -1], 1, -1)