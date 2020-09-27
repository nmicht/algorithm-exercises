class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        acu = nums[0]
        
        for v in nums[1:]:
            acu = acu + v
            output.append(acu)
        
        # print(output)
        
        return output
