def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    in_process = [(tree, False)]

    while in_process:
        node, left_subtree_traversed = in_process.pop()
        if node:
            if left_subtree_traversed:
                result.append(node.data)
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))

    return result