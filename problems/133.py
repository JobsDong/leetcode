#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque


class Solution(object):
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        new_node = UndirectedGraphNode(node.label)

        already_label = dict()

        que = deque()
        que.append(node)
        que2 = deque()
        que2.append(new_node)
        already_label[node.label] = new_node

        while que:
            n = que.popleft()
            n_n = que2.popleft()

            for neighbor in n.neighbors:
                if neighbor.label not in already_label:

                    que.append(neighbor)

                    new_neighbor = UndirectedGraphNode(neighbor.label)
                    already_label[neighbor.label] = new_neighbor
                    n_n.neighbors.append(new_neighbor)
                    que2.append(new_neighbor)
                else:
                    n_n.neighbors.append(already_label[neighbor.label])

        return new_node
