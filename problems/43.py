#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def multiply_one(self, reversed_num, a):
        new_reversed_num = []

        plus = 0
        for i in xrange(0, len(reversed_num)):
            total = a * reversed_num[i]

            new_reversed_num.append((total + plus) % 10)
            plus = (total + plus) / 10

        if plus > 0:
            new_reversed_num.append(plus)

        return new_reversed_num

    def left_move(self, reversed_num, i):
        return [0]*i + reversed_num

    def plus(self, reversed_num1, reversed_num2):
        total = []

        n = len(reversed_num1)
        m = len(reversed_num2)

        plus = 0

        i = 0
        while i < max(n, m):
            if i < n:
                a = reversed_num1[i]
            else:
                a = 0

            if i < m:
                b = reversed_num2[i]
            else:
                b = 0

            total.append((a + b + plus) % 10)
            plus = (a + b + plus) / 10

            i += 1
        if plus > 0:
            total.append(plus)

        return total

    def remove_zero(self, num):

        total = []

        not_add = False
        for i in xrange(len(num)-1, -1, -1):
            if i == len(num)-1 and num[i] == 0:
                not_add = True

            if num[i] != 0:
                not_add = False

            if not not_add:
                total.append(num[i])

        if len(total) == 0:
            return "0"
        else:
            return "".join([str(c) for c in total])


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            reversed_num1 = [int(num2[i]) for i in xrange(len(num2)-1, -1, -1)]
            reversed_num2 = [int(num1[i]) for i in xrange(len(num1)-1, -1, -1)]
        else:
            reversed_num1 = [int(num1[i]) for i in xrange(len(num1)-1, -1, -1)]
            reversed_num2 = [int(num2[i]) for i in xrange(len(num2)-1, -1, -1)]

        m = len(reversed_num2)

        total = []

        for i in xrange(0, m):
            new_reversed_num = self.multiply_one(reversed_num1, reversed_num2[i])
            total = self.plus(total, self.left_move(new_reversed_num, i))

        return self.remove_zero(total)


if __name__ == "__main__":
    # print Solution().left_move([1, 2, 3, 4], 2)
    # print Solution().multiply_one([1, 2, 3, 4], 5)
    # print Solution().remove_zero([1, 0, 0, 1, 0])
    print Solution().multiply("102", "10")