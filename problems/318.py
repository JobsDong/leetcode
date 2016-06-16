#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def word_to_int(self, word):
        m = 0
        for x in word:
            m |= 1 << (ord(x)-ord('a'))
        return m

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_num = len(words)
        ints = []
        lens = []

        for i, word in enumerate(words):
            ints.append(self.word_to_int(word))
            lens.append(len(word))

        max_ = 0
        for j in xrange(0, word_num):
            for k in xrange(j+1, word_num):
                if ints[j] & ints[k] == 0:
                    len_mul = lens[j] * lens[k]
                    if max_ < len_mul:
                        max_ = len_mul

        return max_


if __name__ == "__main__":
    print Solution().maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"])