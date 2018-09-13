# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

# TODO: this example has errors: not matching the "all of the same length" requirements, but
still valid problem, only more difficult for a generalized problems: different length, multiple existense
'''
class ChNodes:
    def __init__(self, c):
        self.c = c
        self.next = {}
        self.wordend = False

    def addnextchar(self, n):
        self.next[n.c] = n

    def get(self, c):
        return self.next.get(c)

class ChTrie(ChNodes):
    def __init__(self):
        # self.nodes = {}
        self.c = None
        self.next = {}
        self.wordend = False
        self.sequence = []
        self.lastnode = None
        self.multimatch = False
        self.count = 0
    def getwordidbycs(self, c):
        # trie with sequence state
        # return if mismatched sequence: False, clear state
        # return if matched sequence: True, state update: last node
        # if has one fully matched sequence: clear state
        # if has multiple match with wordend: int
        # if forward matched with retrieve: -int
        retrieve = False

        if self.lastnode is None:
            d = self.get(c)
            # start new check from head    
        elif not self.multimatch and self.lastnode is not None:
            d = self.lastnode.get(c)
        
        elif self.multimatch and self.lastnode is not None:
            d = self.lastnode.get(c)
            if d is None:  # if multi match failed, not break, alternative find
                self.sequence.clear()
                self.multimatch = False
                d = self.get(c)
            elif d is not None:
                # continued sequence; retrieve the last id
                retrieve = 0 - self.lastnode.wordend
        else:
            print('%s' % c)
            d = None
                
        if d is not None and not d.wordend:
            self.lastnode = d
            self.sequence.append(c)
            return True if not retrieve else retrieve

        elif d is not None and d.wordend:
            if len(d.next) == 0:
                # endnode, clear
                self.lastnode = None
                self.sequence.clear
                self.multimatch = False
                if retrieve:
                    return '%s.%s' % (retrieve, d.wordend)
                else:
                    return d.wordend
            elif len(d.next) > 0:
                # more than one word match
                self.lastnode = d
                self.sequence.append(c)
                multi_match = ''.join(self.sequence)
                self.multimatch = True
                # self.sequence.clear()
                if retrieve:
                    return '%s,%s' % (retrieve, d.wordend)
                else:
                    return d.wordend
            
        elif d is None:
            # broken sequence
            self.sequence.clear()
            self.lastnode = None
            self.multimatch = False
            return False
        else:
            self.sequence.clear()
            self.lastnode = None
            self.multimatch = False
            return False
        
        return False    
        
    def addword(self, s):
        # add a contained s
        # return id
        self.count += 1
        nth = self.count
        d = self.next
        for i in range(len(s)):
            c = s[i]
            p = d.get(c)
            if i == 0 and len(s) >1 and p is None:
                p = ChNodes(c)
                self.addnextchar(p)
                # print('ini %s' % c)
                d = p
            elif i == len(s)-1 and p is None:
                #add wordend propertie
                # print('end %s' % c)
                p = ChNodes(c)
                p.wordend = nth 
                if i == 0:
                    self.addnextchar(p)
                else:
                    d.addnextchar(p)
                d = p
            elif p is not None:
                d = p
            else:
                p = ChNodes(c)
                d.addnextchar(p)
                d = p

        return nth 

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        t = ChTrie()
        word_ids = set([])
        for el in words:
            word_ids.add(t.addword(el))

        sum_lenth = len(''.join(words))
        # print('%s' % word_ids)
        final_result = []
        wordset = set([])
        for i in range(len(s)):
            c = s[i]
            p = t.getwordidbycs(c)
            
            if p is True:
                continue
            elif p is False:
                # clear state
                wordset.clear()
            elif isinstance(p, int):
                if p >= 0:
                    wordset.add(p)
                    # print("add %s" % p)
                else:
                    wordset.remove(-p)
            elif isinstance(p, str):
                l = p.split('.')
                s1 = 0 - int(l[0])
                wordset.remove(s1)
                s2 = int(l[1])
                wordset.add(s2)
            
            if wordset == word_ids:
                final_result.append(i-sum_lenth+1)
                wordset.clear()

        return final_result
                

class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().findSubstring(
                'barfoothefoobarman',
                ["foo","bar"]
            ),
            [0,9]
        )
    def test2(self):
        self.assertCountEqual(
            Solution().findSubstring(
                'wordgoodstudentgoodword',
                ["word","student"]
            ),
            []
        )