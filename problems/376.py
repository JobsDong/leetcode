#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0:
            return 0
        bs = [0]
        count = [1]

        for i in xrange(1, n):

            max_c = 1
            max_b = 0
            for j in xrange(0, i):
                if nums[j] > nums[i] and bs[j] >= 0:
                    c = count[j] + 1
                    b = -1
                elif nums[j] < nums[i] and bs[j] <= 0:
                    c = count[j] + 1
                    b = 1
                else:
                    c = None

                if c is not None:
                    if c > max_c:
                        max_c = c
                        max_b = b
                    elif c == max_c & b * max_b == -1:
                        max_b = 0

            bs.append(max_b)
            count.append(max_c)

        return max(count)


if __name__ == "__main__":
    # print Solution().wiggleMaxLength([1,7,4,9,2,5])
    # print Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    # print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])
    print Solution().wiggleMaxLength([0, 0])