# SOLVED
# https: // leetcode.com/problems/find-all-duplicates-in-an-array/

from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return [k for k in d.keys() if d[k] > 1]

        # f = Counter(nums)
        # return [k for k,v in f.items() if f[k] > 1]
