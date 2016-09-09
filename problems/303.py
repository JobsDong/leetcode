#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        if self.n != 0:
            self.seg_tree = [0] * (4*self.n-1)
            self.build_seg_tree(0, nums, 0, self.n-1)

    def build_seg_tree(self, root, nums, start, end):
        if start == end:
            self.seg_tree[root] = nums[start]
        else:
            mid = (start+end)/2
            self.build_seg_tree(root*2+1, nums, start, mid)
            self.build_seg_tree(root*2+2, nums, mid+1, end)
            self.seg_tree[root] = self.seg_tree[root*2+1] + self.seg_tree[root*2+2]

    def sum_range(self, root, s_start, s_end, start, end):
        mid = (s_start + s_end) / 2
        if s_start == start and s_end == end:
            return self.seg_tree[root]
        elif mid+1 <= start:
            return self.sum_range(root*2+2, mid+1, s_end, start, end)
        elif end <= mid:
            return self.sum_range(root*2+1, s_start, mid, start, end)
        else:
            return self.sum_range(root*2+1, s_start, mid, start, mid) \
                   + self.sum_range(root*2+2, mid+1, s_end, mid+1, end)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0
        return self.sum_range(0, 0, self.n-1, i, j)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == "__main__":
    n = NumArray([1]*10000)