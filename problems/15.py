#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        d_nums = []

        num_count = dict()
        for num in nums:
            if num in num_count:
                num_count[num] += 1
                if num_count[num] <= 2:
                    d_nums.append(num)
            else:
                num_count[num] = 1
                d_nums.append(num)

        array_set = dict()
        arrays = []

        for i in xrange(0, len(d_nums)):
            if d_nums[i] > 0:
                break
            for j in xrange(i+1, len(d_nums)):
                if d_nums[i] + d_nums[j] > 0:
                    break
                for k in xrange(j+1, len(d_nums)):
                    if d_nums[i] + d_nums[j] + d_nums[k] > 0:
                        break
                    if d_nums[i] + d_nums[j] + d_nums[k] == 0:
                        if d_nums[i] in array_set and d_nums[j] in array_set[d_nums[i]]:
                            pass
                        else:
                            arrays.append([d_nums[i], d_nums[j], d_nums[k]])
                            if d_nums[i] not in array_set:
                                array_set[d_nums[i]] = set([d_nums[j]])
                            else:
                                if d_nums[j] not in array_set[d_nums[i]]:
                                    array_set[d_nums[i]].add(d_nums[j])
                            break

        if 0 in num_count and num_count[0] >= 3:
            if 0 in array_set and 0 in array_set[0]:
                pass
            else:
                arrays.append([0, 0, 0])

        return arrays


if __name__ == "__main__":
    print Solution().threeSum([])



