# Find Duplicate in Array
# SOLVED
# https://www.interviewbit.com/problems/find-duplicate-in-array/


import operator


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        d = {}

        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return max(d.items(), key=operator.itemgetter(1))[0]
