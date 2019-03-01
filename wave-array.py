# SOLVED
# https://www.interviewbit.com/problems/wave-array/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(0, len(A) - 1):
            if i % 2 == 0  and A[i] < A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
            elif i % 2 != 0 and A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

        return A

x = Solution()
print(x.wave([1,2]))