#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kd = dict()

        for i, num in enumerate(nums):
            if num not in kd:
                kd[num] = [i]
            else:
                kd[num].append(i)

        for i, num in enumerate(nums):
            left = target-num
            if left in kd:
                if num == left:
                    if len(kd[left]) > 1:
                        return [kd[left][0], kd[left][1]]
                else:
                    return [i, kd[left][0]]
