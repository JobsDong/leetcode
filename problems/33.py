#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)/2
            # print nums[start:end+1], nums[mid]
            if nums[end] >= nums[start]:
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    return mid
            else:
                # print target, nums[end], nums[start], nums[mid]

                if target == nums[end]:
                    return end
                elif target == nums[start]:
                    return start
                elif target == nums[mid]:
                    return mid

                if nums[mid] >= nums[start]:
                    if target > nums[mid] or target < nums[end]:
                        start = mid+1
                    else:
                        end = mid-1
                else:
                    if nums[mid] < target <= nums[end]:
                        start = mid+1
                    else:
                        end = mid-1
        return -1


if __name__ == '__main__':
    print Solution().search([5,1,2,3,4], 1)