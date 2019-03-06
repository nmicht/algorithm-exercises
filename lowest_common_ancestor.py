# Design an algorithm for computing the LCA (lowest common ancestor) of two nodes in a binary tree in which nodes do not have a parent field.
# The LCA is the node furthest from the root that is an ancestor of both nodes.

import collections

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    Status = collections.namedtuple(
        'Status', ('num_target_nodes', 'ancestor')
    )

    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(0, None) # the base case

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes + (node0, node1).count(tree) # how many times node0 and node1 are present in the tree
        )

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor        