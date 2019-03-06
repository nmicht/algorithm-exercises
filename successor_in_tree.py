# The successor of a node in a binary tree is the node that appears immediately after the given node in an inorder traversal.

def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node.right:
        node = node.right 
        while node.left:
            node = node.left
        return node

    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent