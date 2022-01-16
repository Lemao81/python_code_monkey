from models.binary_tree import BinaryTree
from models.binary_tree_node import BinaryTreeNode
from typing import List


def sort_graphs_topologically(unsorted: List, sorted: List):
    without_links = list(filter(lambda x: len(x.adjacent) == 0, unsorted))
    if len(without_links) == 0:
        raise ValueError()
    for graph in without_links:
        sorted.append(graph)
        unsorted.remove(graph)
        for graph2 in unsorted:
            if graph in graph2.adjacent:
                graph2.adjacent.remove(graph)

    if len(unsorted) > 0:
        sort_graphs_topologically(unsorted, sorted)

    return sorted


def find_common_ancestor_in_binary_tree_by_parent_linking(first: BinaryTreeNode, second: BinaryTreeNode, tree_root: BinaryTreeNode) -> BinaryTreeNode:
    first_runner = first
    second_runner = second
    while True:
        if first_runner is second_runner:
            return first_runner
        tree_root.parent = first
        first_runner = first_runner.parent
        tree_root.parent = second
        second_runner = second_runner.parent


def find_common_ancestor_in_binary_tree_by_traversal(first: BinaryTreeNode, second: BinaryTreeNode, tree: BinaryTree) -> BinaryTreeNode:
    def check_are_sub_nodes(potential_ancestor: BinaryTreeNode) -> bool:
        first_node_found = False
        second_node_found = False

        def check_sub_node_recursive(node: BinaryTreeNode):
            nonlocal first_node_found
            nonlocal second_node_found
            if node is None:
                return
            if node is first:
                first_node_found = True
            if node is second:
                second_node_found = True
            if first_node_found and second_node_found:
                return
            check_sub_node_recursive(node.left)
            if first_node_found and second_node_found:
                return
            check_sub_node_recursive(node.right)

        check_sub_node_recursive(potential_ancestor)

        return first_node_found and second_node_found

    return tree.find_first_post_order(check_are_sub_nodes)


def check_is_subtree_of(container: BinaryTree, sub_candidate: BinaryTree) -> bool:
    candidates = container.find_all_in_order(lambda x: x.value == sub_candidate.root.value)
    for candidate in candidates:
        if _check_is_subtree_of_recursive(container.root, candidate):
            return True
    return False


def _check_is_subtree_of_recursive(first: BinaryTreeNode, second: BinaryTreeNode) -> bool:
    if first is None and second is None:
        return True
    if first is not None or second is not None or first.value != second.value:
        return False
    return _check_is_subtree_of_recursive(first.left, second.left) and _check_is_subtree_of_recursive(first.right, second.right)
