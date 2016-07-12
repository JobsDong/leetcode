#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_str = version1.split(".")
        version1_n = len(version1_str)
        version2_str = version2.split(".")
        version2_n = len(version2_str)

        if version1_n < version2_n:
            for i in xrange(version2_n-version1_n):
                version1_str.append("0")
        else:
            for i in xrange(version1_n-version2_n):
                version2_str.append("0")
        print version1_str, version2_str

        for i in xrange(0, len(version1_str)):
            if int(version1_str[i]) > int(version2_str[i]):
                return 1
            elif int(version2_str[i]) > int(version1_str[i]):
                return -1

        return 0


if __name__ == "__main__":
    # print Solution().compareVersion("1.2", "1.1")
    # print Solution().compareVersion("1.0", "1")
    print Solution().compareVersion("01", "1")