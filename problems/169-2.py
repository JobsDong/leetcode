#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candidate = None
        count = 0

        for i in xrange(0, len(nums)):
            if candidate is None:
                candidate = nums[i]
                count = 1
            else:
                if candidate == nums[i]:
                    count += 1
                else:
                    count -= 1

                    if count == 0:
                        candidate = None

        return candidate

