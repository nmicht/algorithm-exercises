# SOLVED
# https: // www.interviewbit.com/problems/max-sum-contiguous-subarray/
# https: // leetcode.com/problems/maximum-subarray/

from collections import deque

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        dp = deque()
        size = len(A)
        if size == 0:
            return 0
        
        dp.append(A[0])
        for i in range(1, size):
            dp.append(max(A[i] + dp[i-1], A[i]))

        return max(dp)

x = Solution()
print(x.maxSubArray([-163, -20]))
