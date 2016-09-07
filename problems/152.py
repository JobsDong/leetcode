#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        has_zero = False
        if nums[0] < 0:
            n_l1 = nums[0]
            p_l1 = None
            max_p_l = nums[0]
        else:
            n_l1 = None
            p_l1 = nums[0]
            max_p_l = nums[0]

        for i in xrange(1, len(nums)):
            if nums[i] > 0:
                n_l1 = n_l1 * nums[i] if n_l1 else None
                t = [nums[i]]
                if p_l1:
                    t.append(p_l1 * nums[i])
                p_l1 = max(t)
            elif nums[i] < 0:
                l_p_l1 = p_l1
                p_l1 = n_l1 * nums[i] if n_l1 else None
                t = [nums[i]]
                if l_p_l1:
                    t.append(l_p_l1 * nums[i])
                n_l1 = min(t)
            else:
                has_zero = True
                p_l1, n_l1 = None, None

            if p_l1:
                max_p_l = max_p_l if max_p_l > p_l1 else p_l1
            if has_zero:
                max_p_l = max(max_p_l, 0)

        return max_p_l

if __name__ == "__main__":
    print Solution().maxProduct([3, -1, 4])