#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        can_dict = {}

        for num in nums:
            if num in can_dict:
                can_dict[num] += 1
            else:
                if len(can_dict) <= 1:
                    can_dict[num] = 1
                else:
                    for k, v in can_dict.items():
                        if v == 1:
                            del can_dict[k]
                        else:
                            can_dict[k] -= 1

        for k, v in can_dict.items():
            can_dict[k] = 0

        for num in nums:
            if num in can_dict:
                can_dict[num] += 1

        for k, v in can_dict.items():
            if v <= len(nums) / 3:
                del can_dict[k]

        return can_dict.keys()