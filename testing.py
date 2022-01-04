from common import create_random_binary_tree
from code_challenges import find_common_ancestor_in_binary_tree_by_parent_linking, find_common_ancestor_in_binary_tree_by_traversal

if __name__ == '__main__':
    tree = create_random_binary_tree(5)
    tree.print()
    first_node = tree.root.right.left
    second_node = tree.root.right.left.right.left

    ancestor_by_linking = find_common_ancestor_in_binary_tree_by_parent_linking(first_node, second_node, tree.root)
    ancestor_by_traversal = find_common_ancestor_in_binary_tree_by_traversal(first_node, second_node, tree)
    pass
