#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop() * 1.0

                if token == '+':
                    stack.append(int(num1 + num2))
                elif token == '-':
                    stack.append(int(num1 - num2))
                elif token == '*':
                    stack.append(int(num1 * num2))
                elif token == '/':
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack[0]



if __name__ == "__main__":
    # print Solution().evalRPN(["2", "1", "+", "3", "*"])
    # print Solution().evalRPN(["4", "13", "5", "/", "+"])
    print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])