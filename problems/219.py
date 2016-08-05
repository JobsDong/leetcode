#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()

        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
                else:
                    d[num] = i
            else:
                d[num] = i

        return False

if __name__ == "__main__":
    print Solution().containsNearbyDuplicate([99, 99], 2)