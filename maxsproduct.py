# https://www.interviewbit.com/problems/maxspprod/
# SOLVED

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        msp = [0]
        size = len(A)

        if size < 3:
            return 0

        for i in range(1, size - 1):
            # search for left
            left = 0
            right = 0
            for j in range(i-1, 0, -1):
                if A[j] > A[i]:
                    left = j
                    break
            if left > 0:
                # search for right
                for j in range(i+1, size):
                    if A[j] > A[i]:
                        right = j
                        break

            msp.append(left*right)

        return max(msp)
