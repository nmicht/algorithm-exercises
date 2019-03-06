# SOLVED
# https://leetcode.com/problems/move-zeroes/submissions/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zero_count = 0

        for i in range(size):
            if nums[i] == 0:
                zero_count += 1
            elif zero_count > 0:
                nums[i - zero_count] = nums[i]
                nums[i] = 0
