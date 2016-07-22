#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


import re

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign_stack = []
        int_stack = []

        items = re.compile("\d+|[\+\-\*/]").findall(s) + ["$"]

        i = 0
        while i < len(items):
            if items[i].isdigit():
                int_stack.append(int(items[i]))
                i += 1
            else:
                if len(sign_stack) <= 0:
                    sign_stack.append(items[i])
                    i += 1
                else:
                    p = sign_stack[len(sign_stack)-1]

                    while p:
                        if p == '+':
                            if items[i] in ['+', '-', '$']:
                                sign_stack.pop()
                                int_stack.append(int_stack.pop() + int_stack.pop())
                            else:
                                break
                        if p == '-':
                            if items[i] in ['+', '-', '$']:
                                sign_stack.pop()
                                int_stack.append(int_stack.pop() * -1 + int_stack.pop())
                            else:
                                break
                        if p == '*':
                            if items[i] in ['+', '-', '*', '/', '$']:
                                sign_stack.pop()
                                int_stack.append(int_stack.pop() * int_stack.pop())
                            else:
                                break
                        if p == '/':
                            if items[i] in ['+', '-', '*', '/', '$']:
                                sign_stack.pop()
                                num2 = int_stack.pop()
                                num1 = int_stack.pop()
                                int_stack.append(num1/num2)
                            else:
                                break

                        if len(sign_stack) <= 0:
                            break
                        else:
                            p = sign_stack[len(sign_stack)-1]

                    sign_stack.append(items[i])
                    i += 1

        return int(int_stack[0])

if __name__ == "__main__":
    print Solution().calculate("2+3*4*2+4*4/2")