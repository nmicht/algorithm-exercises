# Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        valids = []
        count = 0;

        for i in s:
            if i == '(':
                valids.append(i)
            else:
                if valids:
                    valids.pop()
                    count += 2;

        return count;
