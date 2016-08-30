#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def next_word_set(self, word):
        word_set = set()
        for i in xrange(0, len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch != word[i]:
                    new_word = word[:i] + ch + word[i+1:]
                    word_set.add(new_word)

        return word_set

    def ladderLength(self, begin_word, end_word, word_set):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        end_word_pre_set = self.next_word_set(end_word) & word_set

        front = set([begin_word])

        length = 2
        while True:
            if end_word_pre_set & front:
                return length

            new_front = set()
            for word in front:
                new_front |= self.next_word_set(word) & word_set

            if len(new_front) == 0:
                break

            front = new_front
            length += 1
            word_set -= front

        return 0
