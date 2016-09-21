#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        n = len(s)
        nums = []
        for i in xrange(n-1, -1, -1):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            nums.append(d[s[i]])

        nums = nums[-1::-1]

        result = []
        already_c_set = set()

        i = 0
        min_c = None
        while i < n:

            if s[i] not in already_c_set:
                if min_c is None or min_c > s[i]:
                    min_c = s[i]
                    min_i = i

                if nums[i] == 1:
                    already_c_set.add(min_c)
                    result.append(min_c)
                    i = min_i
                    min_c = None

            i += 1

        return "".join(result)

if __name__ == "__main__":
    print Solution().removeDuplicateLetters("")