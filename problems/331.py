#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class TreeNode(object):
    def __init__(self, text):
        self.text = text
        self.count = 0


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#':
            return True

        stack = []
        splits = preorder.split(",")
        for i, split in enumerate(splits):
            split = split.strip()
            if split == '#':
                if len(stack) <= 0:
                    return False

                stack[len(stack)-1].count += 1
                if stack[len(stack)-1].count > 2:
                    return False

                while stack[len(stack)-1].count == 2:
                    stack.pop()
                    if len(stack) <= 0:
                        break
                    stack[len(stack)-1].count += 1
                    if stack[len(stack)-1].count > 2:
                        return False
            else:
                stack.append(TreeNode(split))

            if len(stack) == 0 and i < len(splits) - 1:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    print Solution().isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#")