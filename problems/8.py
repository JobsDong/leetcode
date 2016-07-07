#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_str = re.search("^\s*[-+]?\d+", str)
        if int_str:
            str_int = int(int_str.group(0))
            if str_int > 2147483647:
                return 2147483647
            elif str_int < -2147483648:
                return -2147483648
            else:
                return str_int
        else:
            return 0


if __name__ == "__main__":
    print Solution().myAtoi("   010")