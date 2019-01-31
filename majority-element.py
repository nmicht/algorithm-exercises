# Majority Element
# https://leetcode.com/problems/majority-element/

from collections import Counter

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # majorityCount = 0
        # majorityNumber = 0
        #
        # x = Counter(nums)
        # for k,v in x.items():
        #     if v > majorityCount:
        #         majorityCount = v
        #         majorityNumber = k
        #
        # return majorityNumber

        return Counter(nums).most_common(1)[0][0]
