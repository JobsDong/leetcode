#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        split_paths = path.split("/")
        for split_path in split_paths:
            if split_path == "":
                pass
            elif split_path == ".":
                pass
            elif split_path == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(split_path)

        return "/" + "/".join(stack)

if __name__ == "__main__":
    print Solution().simplifyPath("")