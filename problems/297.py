#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        l = []
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                l.append("null")
            else:
                l.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return str(",".join(l))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split(",")

        if len(l) <= 0 or l[0] == 'null':
            return None

        queue = deque()
        i = 0
        root = TreeNode(str(l[0]))
        queue.append(root)

        while len(queue) > 0 and i < len(l):
            node = queue.popleft()
            if i+1 < len(l) and l[i+1] != 'null':
                node.left = TreeNode(str(l[i+1]))
                queue.append(node.left)
            if i+2 < len(l) and l[i+2] != 'null':
                node.right = TreeNode(str(l[i+2]))
                queue.append(node.right)
            i += 2

        return root



if __name__ == "__main__":
    codec = Codec()
    root = codec.deserialize("1,2,3,null,null,4,5,null,null,null,null")
    print codec.serialize(root)
    # print root.val, root.left.val, root.right.val, root.left.left

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))