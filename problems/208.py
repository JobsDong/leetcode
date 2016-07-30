#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = dict()


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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

        p.children['$'] = None


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        if '$' in p.children:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]

        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("ab")
    print trie.search("a")
    print trie.startsWith("a")