#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

from collections import deque


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        input_d = dict()
        output_value = dict()

        for prerequisite in prerequisites:
            if prerequisite[0] not in output_value:
                output_value[prerequisite[0]] = set()

            if prerequisite[1] not in output_value[prerequisite[0]]:
                output_value[prerequisite[0]].add(prerequisite[1])

                if prerequisite[1] not in output_value:
                    output_value[prerequisite[1]] = set()

                if prerequisite[1] not in input_d:
                    input_d[prerequisite[1]] = 0
                input_d[prerequisite[1]] += 1

                if prerequisite[0] not in input_d:
                    input_d[prerequisite[0]] = 0

        queue = deque()
        for key, value in input_d.items():
            if value == 0:
                queue.append(key)

        while queue:
            item = queue.popleft()
            for v in output_value[item]:
                input_d[v] -= 1
                if input_d[v] == 0:
                    queue.append(v)


        for v in input_d.values():
            if v != 0:
                return False
        return True

if __name__ == "__main__":
    print Solution().canFinish(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])