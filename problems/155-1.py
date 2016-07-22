#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() is None or x <= self.getMin():
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.getMin()))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1][1]
        else:
            return None

