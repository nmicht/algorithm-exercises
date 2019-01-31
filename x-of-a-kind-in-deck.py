# X of a Kind in a deck of cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        c = Counter(deck) # counting for each item
        s = set([v for k,v in c.items()]) # list comprenhension and taking duplicated with set
        return reduce(gcd, s) >= 2 # reduce for each combination runs math.gcd
