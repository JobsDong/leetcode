#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import re
import operator

class Solution(object):

    def tab(self, tokens, start, n):
        if n == 1:
            return [tokens[start]]

        results = []
        for i in xrange(start+1, start+n, 2):
            s1 = self.tab(tokens, start, i-start)
            s2 = self.tab(tokens, i+1, start+n-i-1)

            for r1 in s1:
                for r2 in s2:
                   results.append(tokens[i](r1, r2))
        return results

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split("(\D)", input)
        d = {"-": operator.sub, "+": operator.add, "*": operator.mul}
        o = lambda x: d[x] if x in d else int(x)
        tokens = [o(item) for item in tokens]

        return self.tab(tokens, 0, len(tokens))


if __name__ == "__main__":
    print Solution().diffWaysToCompute("2*3-4*5")