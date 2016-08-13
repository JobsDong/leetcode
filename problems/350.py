#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']



class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            n1 = nums1
            n2 = nums2
        else:
            n1 = nums2
            n2 = nums1

        res = []
        for c in n2:
            if c in n1:
                res.append(c)
                n1.remove(c)

        return res

if __name__ == "__main__":
    print Solution().intersect([1, 2, 2, 1], [2, 2])