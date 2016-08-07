#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = dict()
        for i, c in enumerate(secret):
            if c not in d:
                d[c] = set()
            d[c].add(i)


        bulls = 0
        cows = 0

        i = 0
        while i < len(guess):
            if guess[i] == secret[i]:
                if i in d[secret[i]]:
                    d[secret[i]].remove(i)
                bulls += 1

            i += 1


        for key in d.keys():
            d[key] = len(d[key])


        i = 0
        while i < len(guess):
            if guess[i] != secret[i] and guess[i] in d and d[guess[i]] > 0:
                d[guess[i]] -= 1
                cows += 1

            i += 1

        return "%dA%dB" % (bulls, cows)


if __name__ == "__main__":
    print Solution().getHint("1123", "0111")
    print Solution().getHint("1122", "2211")
    print Solution().getHint("1234", "0111")