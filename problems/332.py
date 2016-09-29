#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

import collections


class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        t_d = collections.defaultdict(list)
        for ticket in sorted(tickets):
            t_d[ticket[0]].append(ticket[1])

        def build_line(head, line, ticket_dict):
            if head in ticket_dict and ticket_dict[head]:
                for next_head in ticket_dict[head][0:]:
                    next_line = line[0:] + [next_head]
                    temp_list = ticket_dict[head][0:]
                    ticket_dict[head].remove(next_head)
                    result = build_line(next_head, next_line, ticket_dict)
                    ticket_dict[head] = temp_list
                    if result is not None:
                        return result

                return None
            else:
                if len(line) == n+1:
                    return line
                else:
                    return None

        return build_line("JFK", ["JFK"], t_d)

if __name__ == "__main__":
    print Solution().findItinerary([["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]])