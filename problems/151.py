#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import re

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = re.split("\s+", s.strip())
        return " ".join(words[-1::-1])


if __name__ == "__main__":
    print Solution().reverseWords("the sky is blue")