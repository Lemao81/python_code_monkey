from typing import Union

from models.tree_node import BinaryTreeNode

TreeNodeOrNone = Union[BinaryTreeNode, None]


def create_search_tree(array: [int]) -> TreeNodeOrNone:
    array_length = len(array)
    if array_length == 0:
        return None
    (root, left_part, right_part) = split_array(array)
    append_to_search_tree(left_part, root)
    append_to_search_tree(right_part, root)
    return root


def append_to_search_tree(array: [int], node: BinaryTreeNode):
    array_length = len(array)
    if array_length == 0:
        return
    (new_node, left_part, right_part) = split_array(array)
    if new_node.value < node.value:
        node.left = new_node
    else:
        node.right = new_node
    append_to_search_tree(left_part, new_node)
    append_to_search_tree(right_part, new_node)


def split_array(array: [int]) -> (BinaryTreeNode, [int], [int]):
    array_length = len(array)
    mid = array.pop(array_length // 2)
    array_length -= 1
    left_part = []
    right_part = []
    if array_length == 1:
        if array[0] < mid:
            left_part.append(array[0])
        else:
            right_part.append(array[0])
    else:
        left_part = array[:array_length // 2]
        right_part = array[array_length // 2:]
    return BinaryTreeNode(mid), left_part, right_part


def get_minimum_search_tree(array: [int]) -> TreeNodeOrNone:
    array_length = len(array)
    if array_length == 0:
        return None
    mid = array.pop(array_length // 2)
    new_node = BinaryTreeNode(mid)
    array_length -= 1
    if array_length == 1:
        leaf = BinaryTreeNode(array[0])
        new_node.left = leaf if array[0] < mid else None
        new_node.right = leaf if array[0] >= mid else None
    else:
        new_node.left = get_minimum_search_tree(array[:array_length // 2])
        new_node.right = get_minimum_search_tree(array[array_length // 2:])
    return new_node


if __name__ == '__main__':
    values = [2, 4, 5, 7, 10, 12, 23, 45, 60]
    tree = create_search_tree(values)
    tree.print()
    print()
    values2 = [2, 4, 5, 7, 10, 12, 23, 45, 60]
    tree2 = get_minimum_search_tree(values2)
    tree2.print()
