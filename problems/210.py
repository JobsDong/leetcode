#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_cs = [0] * numCourses
        out_vs = dict()

        for prerequisite in prerequisites:

            if prerequisite[0] not in out_vs:
                out_vs[prerequisite[0]] = set()

            if prerequisite[1] not in out_vs[prerequisite[0]]:
                out_vs[prerequisite[0]].add(prerequisite[1])
                in_cs[prerequisite[1]] += 1

        que = deque()
        result = []

        for i in xrange(0, numCourses):
            if in_cs[i] == 0:
                que.append(i)

        while que:
            item = que.popleft()
            result.append(item)
            if item in out_vs:
                for v in out_vs[item]:
                    in_cs[v] -= 1
                    if in_cs[v] == 0:
                        que.append(v)

        for in_c in in_cs:
            if in_c != 0:
                return []

        return result[::-1]

if __name__ == "__main__":
    print Solution().findOrder(3, [[0,2],[1,2],[2,0]])