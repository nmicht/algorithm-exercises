class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        leftRunningSum = [A[0]]
        rightRunningSum = []
        currentSum = 0
        
        for j in range(1,len(A)):
            leftRunningSum.append(A[j]+leftRunningSum[j-1])
        
        
        for i in range(len(A), 1, -1):
            previousIndex = len(A) - i
            currentSum = A[i-1]+currentSum
            rightRunningSum.append(currentSum)
            
            try:
                # print("searching currentSum: ", currentSum)
                matchingValueIndex = leftRunningSum[:i-1].index(currentSum)
                # print("leftArray:", leftRunningSum, "rightArray: ", rightRunningSum)
                
                # get the middle sum
                if matchingValueIndex+1 < i-1:
                    middleArray = A[matchingValueIndex+1:i-1]
                    # print("middleArray: ", middleArray)
                    middleSum = sum(middleArray)
                    # print("matchinValueIndex:", matchingValueIndex, "middleSum:", middleSum)

                    if middleSum == currentSum:
                        return True
                else:
                    return False
            except ValueError:
                continue
        
        return False
