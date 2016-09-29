#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = dict()

        for i, equation in enumerate(equations):

            if equation[0] not in d:
                d[equation[0]] = dict()

            if equation[1] not in d[equation[0]]:
                d[equation[0]][equation[1]] = values[i]

            if equation[1] not in d:
                d[equation[1]] = dict()

            if equation[1] not in d[equation[1]]:
                if values[i] != 0.0:
                    d[equation[1]][equation[0]] = 1/values[i]

        total = [1.0]
        ks = set()

        def dfs(head, end):
            if head not in d or end not in d or (head, end) in ks:
                return False

            if end in d[head]:
                total[0] *= d[head][end]
                return True
            else:
                for key, value in d[head].items():
                    if (head, key) not in ks:
                        total[0] *= value
                        ks.add((head, key))
                        if dfs(key, end):
                            return True
                        else:
                            ks.remove((head, key))
                            total[0] /= value

                return False

        results = []
        for query in queries:
            if dfs(query[0], query[1]):
                results.append(total[0])
            else:
                results.append(-1.0)

            total[0] = 1.0
            ks = set()

        return results

if __name__ == "__main__":
    print Solution().calcEquation([["a","b"],["b","c"]], [2.0, 3.0], [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]])
