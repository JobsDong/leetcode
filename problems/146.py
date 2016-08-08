#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Node(object):

    def __init__(self):
        self.key = None
        self.val = None
        self.left = None
        self.right = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # capacity
        self.capacity = capacity
        # dict
        self.d = dict()
        # linked list
        self.root = Node()
        self.root.key = "root"

        self.tail = Node()
        self.tail.key = "tail"
        self.root.right = self.tail
        self.tail.left = self.root

    def _move_to_tail(self, node):
        node.left.right = node.right
        node.right.left = node.left

        self.tail.left.right = node
        node.left = self.tail.left
        self.tail.left = node
        node.right = self.tail


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.d:
            return -1

        node = self.d[key]
        self._move_to_tail(node)
        return node.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.d:
            node = Node()
            node.key = key
            node.val = value
            node.right = self.tail
            node.left = self.tail.left
            self.tail.left.right = node
            self.tail.left = node
            self.d[key] = node

            if len(self.d) > self.capacity:
                remove_node = self.root.right
                self.root.right = remove_node.right
                remove_node.right.left = self.root
                del self.d[remove_node.key]

        else:
            node = self.d[key]
            node.val = value
            self._move_to_tail(node)


if __name__ == "__main__":
    cache = LRUCache(1)
    cache.set(2, 1)
    print cache.get(2)
