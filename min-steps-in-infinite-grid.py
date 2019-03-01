# SOLVED
# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            temp1 = abs(A[i]-A[i-1])
            temp2 = abs(B[i]-B[i-1])
            steps += max(temp1, temp2)

        return steps

x = Solution()
print(x.coverPoints([-7, -13],[1, -5]))
