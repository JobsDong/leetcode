#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def __init__(self):
        self._c2i = dict()

    def word_2_int(self, word):
        sum = 0
        for x in word:
            if x not in self._c2i:
                self._c2i[x] = 1 << (ord(x) - ord('a'))
            sum |= self._c2i[x]
        return sum

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, cmp=lambda x, y: len(y)-len(x))

        word_num = len(words)
        ints = []
        lens = []

        for i, word in enumerate(words):
            ints.append(self.word_2_int(word))
            lens.append(len(word))

        max_ = 0
        for j in xrange(0, word_num):
            for k in xrange(j+1, word_num):
                if ints[j] & ints[k] == 0:
                    len_mul = lens[j] * lens[k]
                    if max_ < len_mul:
                        max_ = len_mul
                    break

        return max_