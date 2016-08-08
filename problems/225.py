#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        n = len(self.queue)

        while n > 1:
            num = self.queue.popleft()
            self.queue.append(num)
            n -= 1


    def pop(self):
        """
        :rtype: nothing
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.pop()
    print s.pop()
    print s.pop()