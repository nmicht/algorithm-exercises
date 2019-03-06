# InOrder: left, root, right

def tree_traversal(root: BinaryTreeNode) -> None:
    if root:
        tree_traversal(root.left)
        print(root.data)
        tree_traversal(root.right)