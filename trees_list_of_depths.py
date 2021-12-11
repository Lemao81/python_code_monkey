from common import create_random_binary_tree
from models.binary_tree_node import BinaryTreeNode
from models.linked_list import LinkedList


def get_depth_level_linked_lists(node: BinaryTreeNode, lists: [], depth_index: int):
    if node is None:
        return
    if len(lists) < depth_index:
        lists.append(LinkedList(node))
    else:
        lists[depth_index - 1].append(node)
    get_depth_level_linked_lists(node.left, lists, depth_index + 1)
    get_depth_level_linked_lists(node.right, lists, depth_index + 1)


if __name__ == '__main__':
    tree = create_random_binary_tree(5)
    depth_level_linked_lists = []
    get_depth_level_linked_lists(tree.root, depth_level_linked_lists, 1)
    for linked_list in depth_level_linked_lists:
        linked_list.print_values()
