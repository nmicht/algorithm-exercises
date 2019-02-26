from collections import deque

# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t1_queue = deque()
        t2_queue = deque()
        t1_queue.append(t1)
        t2_queue.append(t2)
        count = 1
        result = TreeNode(None)
        current_result = result
        parent = result

        while(t1_queue or t2_queue):
            current_t1 = None
            current_t2 = None
            ct1v = 0
            ct2v = 0

            if t1_queue:
                current_t1 = t1_queue.popleft()
            if t2_queue:
                current_t2 = t2_queue.popleft()

            # print(current_t1.val, current_t2.val)

            if current_t1:
                ct1v = current_t1.val
                if current_t1.left:
                    t1_queue.append(current_t1.left)
                else:
                    t1_queue.append(None)
                if current_t1.right:
                    t1_queue.append(current_t1.right)
                else:
                    t1_queue.append(None)


            if current_t2:
                ct2v = current_t2.val
                if current_t2.left:
                    t2_queue.append(current_t2.left)
                else:
                    t2_queue.append(None)
                if current_t2.right:
                    t2_queue.append(current_t2.right)
                else:
                    t2_queue.append(None)

            current_result.val = ct1v + ct2v

            if not count % 2 == 0:
                parent.left = TreeNode(None)
                current_result = parent.left
                print('going with left')
            else:
                parent.right = TreeNode(None)
                current_result = parent.right
                parent = parent.left
                print('going with right')

            count += 1

        return result


'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        merged_tree = TreeNode(None)
        t1_queue = deque()
        t2_queue = deque()
        t3_queue = deque()
        t1_queue.append(t1)
        t2_queue.append(t2)
        t3_queue.append(merged_tree)

        while(t1_queue or t2_queue):
            res = 0

            if t1_queue:
                current_t1 = t1_queue.popleft()
            if t2_queue:
                current_t2 = t2_queue.popleft()

            if not current_t1 and not current_t2:
                continue

            result = t3_queue.popleft()


            if current_t1:
                print('tree 1')
                if current_t1.val != None:
                    res += current_t1.val
                print(current_t1.val)
                if current_t1.left:
                    t1_queue.append(current_t1.left)
                    print('add left: ', current_t1.left.val)
                else:
                    t1_queue.append(None)
                    print('add None')
                if current_t1.right:
                    t1_queue.append(current_t1.right)
                    print('add right: ', current_t1.right.val)
                else:
                    t1_queue.append(None)
                    print('add None')


            if current_t2:
                print('tree 2')
                if current_t2.val != None:
                    res += current_t2.val
                print(current_t2.val)
                if current_t2.left:
                    t2_queue.append(current_t2.left)
                    print('add left: ', current_t2.left.val)
                else:
                    t2_queue.append(None)
                    print('add None')
                if current_t2.right:
                    t2_queue.append(current_t2.right)
                    print('add left: ', current_t2.right.val)
                else:
                    t2_queue.append(None)
                    print('add None')

            if current_t1 or current_t2:
                result.val = res
            print('---->', result.val)

            # if (current_t1 and current_t1.left != None) or (current_t2 and current_t2.left != None):
            result.left = TreeNode(None)
            t3_queue.append(result.left)
            print('add result left')
            # if (current_t1 and current_t1.right != None) or (current_t2 and current_t2.right != None):
            result.right = TreeNode(None)
            t3_queue.append(result.right)
            print('add result right')

        return merged_tree
        '''
