#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.nodes = [None] * 4 * len(nums)

        def _build(r, left, right):
            if left == right:
                self.nodes[r] = nums[left]
            else:
                mid = (left+right)/2
                _build(2*r+1, left, mid)
                _build(2*r+2, mid+1, right)
                self.nodes[r] = self.nodes[2*r+1] + self.nodes[2*r+2]

        if len(nums) >= 1:
            _build(0, 0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """

        def _update(r, left, right, add_val):
            if left == right:
                if left == right == i:
                    self.nodes[r] += add_val
                    return
                else:
                    return

            if i < left or i > right:
                return
            if left <= i <= right:
                self.nodes[r] += add_val
                mid = (left+right)/2
                _update(2*r+1, left, mid, add_val)
                _update(2*r+2, mid+1, right, add_val)
                return

        _update(0, 0, len(self.nums)-1, val-self.nums[i])
        self.nums[i] = val


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        def _sum(r, left, right, sl, sr):
            if left > sr or right < sl:
                return 0
            if left >= sl and right <= sr:
                return self.nodes[r]
            mid = (left+right)/2
            return _sum(2*r+1, left, mid, sl, sr) + _sum(2*r+2, mid+1, right, sl, sr)

        return _sum(0, 0, len(self.nums)-1, i, j)

if __name__ == "__main__":
    array = NumArray([7, 2, 7, 2, 0])
    print array.nodes
    array.update(4, 6)
    print array.nodes
    array.update(0, 2)
    print array.nodes
    array.update(0, 9)
    print array.nodes
    print array.sumRange(4, 4)
    array.update(3, 8)
    print array.sumRange(0, 4)
    array.update(4, 1)
    print array.sumRange(0, 3)
    print array.sumRange(0, 4)
    array.update(0, 4)
