#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._in_stack = []
        self._out_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._in_stack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if len(self._out_stack) == 0:
            while len(self._in_stack) > 0:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self._out_stack) == 0:
            while len(self._in_stack) > 0:
                    self._out_stack.append(self._in_stack.pop())

        return self._out_stack[len(self._out_stack)-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self._in_stack) == 0 and len(self._out_stack) == 0


if __name__ == "__main__":
    queue = Queue()
    print queue.empty()
    queue.push(1)
    queue.push(2)
    print queue.peek()
    print queue.pop()
    print queue.peek()
    queue.push(3)
    print queue.peek()
    print queue.pop()
    print queue.pop()