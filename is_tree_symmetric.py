# Write a program that checks whether a binary tree is symmetric
# A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror image of the right subtree

def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True # the base case
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left)
                    )
        return False # one is empty and the other do not

    return not tree or check_symmetric(tree.left, tree.right)