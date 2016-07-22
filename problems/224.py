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
        for x in re.compile("\d+|[\+\-\(\)]").findall(s) + ["$"]:
            if x.isdigit():
                int_stack.append(x)
            elif x in ['+', '-', '(', ')', '$']:
                if len(sign_stack) <= 0:
                    sign_stack.append(x)
                else:
                    p = sign_stack[len(sign_stack)-1]

                    if p == '+':
                        if x in ['-', ')', '+', '$']:
                            num2 = int(int_stack.pop())
                            num1 = int(int_stack.pop())
                            int_stack.append(num1 + num2)
                            sign_stack.pop()
                        if x == ')':
                            sign_stack.pop()
                        else:
                            sign_stack.append(x)
                    elif p == '-':
                        if x in ['+', '-', ')', '$']:
                            num2 = int(int_stack.pop())
                            num1 = int(int_stack.pop())
                            int_stack.append(num1-num2)
                            sign_stack.pop()
                        if x == ')':
                            sign_stack.pop()
                        else:
                            sign_stack.append(x)
                    elif p == '(':
                        if x == ')':
                            sign_stack.pop()
                        else:
                            sign_stack.append(x)
            else:
                pass

        return int(int_stack[0])

if __name__ == "__main__":
    print Solution().calculate("22")