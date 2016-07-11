#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s)-1

        while i < j:

            left_c = s[i]
            while i < j:
                left_c = s[i]
                if left_c.isalnum():
                    break
                else:
                    i += 1

            if i == j:
                break

            right_c = s[j]
            while i < j:
                right_c = s[j]
                if right_c.isalnum():
                    break
                else:
                    j -= 1

            if i == j:
                break

            if left_c.lower() != right_c.lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
    print Solution().isPalindrome("race a car")



