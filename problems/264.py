#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def __init__(self):
        self._ugliy_numbers = list()

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self._ugliy_numbers) >= n:
            return self._ugliy_numbers[n-1]

        self._ugliy_numbers.append(1)

        i = 0
        j = 0
        k = 0

        while len(self._ugliy_numbers) < n:

            ug_2 = 2 * self._ugliy_numbers[i]
            while ug_2 <= self._ugliy_numbers[-1]:
                i += 1
                ug_2 = 2 * self._ugliy_numbers[i]

            ug_3 = 3 * self._ugliy_numbers[j]
            while ug_3 <= self._ugliy_numbers[-1]:
                j += 1
                ug_3 = 3 * self._ugliy_numbers[j]

            ug_5 = 5 * self._ugliy_numbers[k]
            while ug_5 <= self._ugliy_numbers[-1]:
                k += 1
                ug_5 = 5 * self._ugliy_numbers[k]

            min_ug = min(ug_2, ug_3, ug_5)
            self._ugliy_numbers.append(min_ug)
            if min_ug == ug_2:
                i += 1
            elif min_ug == ug_3:
                j += 1
            else:
                k += 1

        return self._ugliy_numbers[n-1]


if __name__ == "__main__":
    print Solution().nthUglyNumber(100)
