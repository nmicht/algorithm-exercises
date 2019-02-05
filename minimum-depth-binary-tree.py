# Minimum depth of binary tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0;

        row = []
        row.append(root)
        level = 1

        while row:
            new_row = []
            for node in row:
                if not node.left and not node.right:
                    return level
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)

            row = new_row
            level += 1
