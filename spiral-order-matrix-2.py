# SOLVED
# https://www.interviewbit.com/problems/spiral-order-matrix-ii/
# https://leetcode.com/problems/spiral-matrix-ii


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        M = [[0 for x in range(A)] for y in range(A)]
        lr = A - 1
        lc = A - 1
        fr = 0
        fc = 0
        count = 1
        
        while fr < A and fc < A:
            for i in range(fc, lc + 1):
                M[fr][i] = count
                count += 1
            fr += 1
            for i in range(fr, lr + 1):
                M[i][lc] = count
                count += 1
            lc -= 1
            for i in range(lc, fc - 1, -1):
                M[lr][i] = count
                count += 1
            lr -= 1
            for i in range(lr, fr - 1, -1):
                M[i][fc] = count
                count += 1
            fc += 1

        return M

x = Solution()
print(x.generateMatrix(3))
