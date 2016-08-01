#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

from collections import deque

class TrieNode(object):

    def __init__(self):
        self.val = None
        self.is_end = False
        self.children = dict()

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if c not in p.children:
                node = TrieNode()
                node.val = c
                p.children[c] = node
            p = p.children[c]

        p.is_end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        p = self.root

        queue = deque()
        queue.append(p)
        queue.append(None)

        for c in word:
            if len(queue) <= 1:
                return False

            while len(queue) > 0:
                node = queue.popleft()
                if node is not None:
                    if c == '.':
                        for key, child in node.children.items():
                            queue.append(child)
                    else:
                        if c in node.children:
                            queue.append(node.children[c])
                else:
                    queue.append(None)
                    break

        while len(queue) > 0:
            node = queue.popleft()
            if node is not None and node.is_end:
                return True

        return False

if __name__ == "__main__":
    word_dict = WordDictionary()
    word_dict.addWord("a")
    print word_dict.search(".")


    # word_dict.addWord("ran")
    # word_dict.addWord("rune")
    # word_dict.addWord("runner")
    # word_dict.addWord("runs")
    # word_dict.addWord("add")
    # word_dict.addWord("adds")
    # word_dict.addWord("adder")
    # word_dict.addWord("addee")
    #
    # print word_dict.search("........")
    # print word_dict.search("..n.r")

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")