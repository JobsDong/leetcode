#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        vs = []
        d = dict()

        for s in strs:
            k = "".join(sorted(s))
            if k in d:
                vs[d[k]].append(s)
            else:
                vs.append([s])
                d[k] = len(vs) - 1

        return vs

if __name__ == "__main__":
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
