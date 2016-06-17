#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_count = dict()
        d_nums = []
        for num in nums:
            if num in num_count:
                num_count[num] += 1
                if num_count[num] <= 3:
                    d_nums.append(num)
            else:
                num_count[num] = 1
                d_nums.append(num)

        nums = sorted(d_nums)
        nice_total = None
        min_fab_dis = None

        i = 0
        while i < len(nums):

            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                dis = total - target
                fab_dis = dis if dis > 0 else -dis

                if min_fab_dis is None or fab_dis < min_fab_dis:
                    min_fab_dis = fab_dis
                    nice_total = total

                if dis > 0:
                    k -= 1
                elif dis < 0:
                    j += 1
                else:
                    return target

            i += 1

        return nice_total

if __name__ == "__main__":
    # print Solution().threeSumClosest([-10,-82,-70,92,39,-98,94,93,27,-74,1,-80,-95,-36,10,-12,43,92,-61,30,-26,100,-35,-54,-91,-58,-73,-66,86,8,1,49,-46,55,-89,39,45,66,96,42,80,-76,-69,53,-75,16,-13,53,-37,98,-59,72,41,-50,-23,-21,91,22,4,-80,1,-89,93,5,82,20,5,-77,95,16,-51,-21,0,-66,-84,-17,6,-65,12,94,-38,1,71,23,-71,50,8,28,80,-47,5,-13,69,-9,13,41,83,-61,-87,-51,89,-10,37,-73,-64,11,49], 215)
    print Solution().threeSumClosest([0, 0, 0], 1)