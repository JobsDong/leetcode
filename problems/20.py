#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if len(stack) <= 0:
                stack.append(c)
            else:
                if stack[len(stack)-1] == '(' and c == ')':
                    stack.pop()
                elif stack[len(stack)-1] == '{' and c == '}':
                    stack.pop()
                elif stack[len(stack)-1] == '[' and c == ']':
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack) == 0

if __name__ == "__main__":
    print Solution().isValid("[]")