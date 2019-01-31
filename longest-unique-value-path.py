# Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        nodesToCheck = [root]
        maxLengthSoFar = 1

        while nodesToCheck:
            currentNode = nodesToCheck.pop()
            currentValue = currentNode.val

            if currentNode.left and currentNode.left.val != currentValue:
                nodesToCheck.append(currentNode.left)

            if currentNode.right and currentNode.right.val != currentValue:
                nodesToCheck.append(currentNode.right)

            maxLengthSoFar = max(maxLengthSoFar, self.maxPathIncludingRoot(currentNode))

        return maxLengthSoFar - 1


    def maxPathIncludingRoot(self, node):
        if not node:
            return 0

        leftMaxPath = 0
        if node.left and node.left.val == node.val:
            leftMaxPath = self.maxPathIncludingRoot(node.left)

        rightMaxPath = 0
        if node.right and node.right.val == node.val:
            rightMaxPath = self.maxPathIncludingRoot(node.right)

        if leftMaxPath and rightMaxPath:
            return rightMaxPath + leftMaxPath + 1

        return max(rightMaxPath, leftMaxPath) + 1
