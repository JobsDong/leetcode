#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def num_to_string(self, num):
        u1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        u2 = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        u3 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        s_b = []
        h = num / 100
        if h > 0:
            s_b.append(u1[h-1])
            s_b.append("Hundred")

        n = num % 100 / 10
        if num % 100 == 10:
            s_b.append("Ten")
        else:
            if n == 0:
                pass
            elif n == 1:
                s_b.append(u2[num % 100 % 10 - 1])
                return " ".join(s_b)
            else:
                s_b.append(u3[n-2])

        m = num % 100 % 10
        if m > 0:
            s_b.append(u1[m-1])

        return " ".join(s_b)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        strs = []
        units = ["Thousand", "Million", "Billion"]

        i = 0
        unit = ""
        while True:

            a = num % 1000
            num_to_s = self.num_to_string(a)
            if len(num_to_s) > 0:
                strs.append(unit)
                strs.append(num_to_s)

            num /= 1000
            if num > 0:
                unit = units[i]
                i += 1
            else:
                break

        return " ".join(strs[-1::-1]).strip()


if __name__ == "__main__":
    print Solution().numberToWords(10)
    print Solution().numberToWords(1000)
    print Solution().numberToWords(1000000)