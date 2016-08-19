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
            # remove duplicate nums
            while start+1 <= end and nums[start] == nums[start+1]:
                start += 1
            while start <= end-1 and nums[end] == nums[end-1]:
                end -= 1

            if start != end and nums[start] == nums[end]:
                start += 1

            mid = (start+end)/2
            # print nums[start:end+1], nums[mid]
            if nums[end] >= nums[start]:
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    return True
            else:
                # print target, nums[end], nums[start], nums[mid]

                if target == nums[end]:
                    return True
                elif target == nums[start]:
                    return True
                elif target == nums[mid]:
                    return True

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
        return False

if __name__ == "__main__":
    print Solution().search([1,1,3,1], 3)