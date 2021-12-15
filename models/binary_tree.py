import math

from models.binary_tree_node import BinaryTreeNode
from typing import Callable

from models.linked_list import LinkedList


class BinaryTree:
    value_length = 2

    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)

    def traverse_pre_order(self, visit: Callable[[BinaryTreeNode], None]):
        self._traverse_pre_order_recursive(self.root, visit)

    def traverse_in_order(self, visit: Callable[[BinaryTreeNode], None]):
        self._traverse_in_order_recursive(self.root, visit)

    def traverse_post_order(self, visit: Callable[[BinaryTreeNode], None]):
        self._traverse_post_order_recursive(self.root, visit)

    def check_pre_order(self, predicate: Callable[[BinaryTreeNode], bool]) -> bool:
        return self._check_pre_order_recursive(self.root, predicate)

    def get_depth(self):
        return self._get_depth_recursive(self.root, 0)

    def is_balanced(self):
        return self.check_pre_order(self._check_balanced)

    def print(self):
        depth = self.get_depth()
        length_small_gap = 2
        length_big_gap = 4
        node_count_bottom = math.pow(2, depth)
        total_length = node_count_bottom * BinaryTree.value_length + node_count_bottom / 2 * length_small_gap + node_count_bottom / 4 * length_big_gap
        depth_level_linked_lists = []
        self._get_depth_level_linked_lists(self.root, depth_level_linked_lists, 1)
        lines = map(lambda x: self._map_depth_level_linked_list_to_print_line(x, math.floor(total_length)), depth_level_linked_lists)
        for line in lines:
            print(line)

    def _traverse_pre_order_recursive(self, node: BinaryTreeNode, visit: Callable[[BinaryTreeNode], None]):
        if node is None:
            return

        visit(node)
        self._traverse_pre_order_recursive(node.left, visit)
        self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_in_order_recursive(self, node: BinaryTreeNode, visit: Callable[[BinaryTreeNode], None]):
        if node is None:
            return

        self._traverse_in_order_recursive(node.left, visit)
        visit(node)
        self._traverse_in_order_recursive(node.right, visit)

    def _traverse_post_order_recursive(self, node: BinaryTreeNode, visit: Callable[[BinaryTreeNode], None]):
        if node is None:
            return

        self._traverse_post_order_recursive(node.left, visit)
        self._traverse_post_order_recursive(node.right, visit)
        visit(node)

    def _check_pre_order_recursive(self, node: BinaryTreeNode, predicate: Callable[[BinaryTreeNode], bool]) -> bool:
        return predicate(node) and (
                node is None or self._check_pre_order_recursive(node.left, predicate) and self._check_pre_order_recursive(node.right, predicate))

    def _get_depth_recursive(self, node: BinaryTreeNode, depth_index: int) -> int:
        if node is None:
            return depth_index - 1

        left_value = self._get_depth_recursive(node.left, depth_index + 1)
        right_value = self._get_depth_recursive(node.right, depth_index + 1)
        return left_value if left_value >= right_value else right_value

    def _get_depth_level_linked_lists(self, node: BinaryTreeNode, lists: [], depth_index: int):
        if node is None:
            return
        if len(lists) < depth_index:
            lists.append(LinkedList(node))
        else:
            lists[depth_index - 1].append(node)
        self._get_depth_level_linked_lists(node.left, lists, depth_index + 1)
        self._get_depth_level_linked_lists(node.right, lists, depth_index + 1)

    def _map_depth_level_linked_list_to_print_line(self, linked_list: LinkedList, total_length: int) -> str:
        result = ''
        count = linked_list.get_count()
        head = linked_list.root
        while head is not None:
            result += str(head.value.value).rjust(2, ' ').center(math.floor(total_length / count), ' ')
            head = head.next
        return result

    def _check_balanced(self, node: BinaryTreeNode) -> bool:
        if node is None:
            return True

        is_terminating = node.left is None and node.right is None
        is_continuing_balanced = node.left is not None and node.right is not None
        is_left_nearly_terminating = node.right is None and node.left is not None and node.left.left is None and node.left.right is None
        is_right_nearly_terminating = node.left is None and node.right is not None and node.right.left is None and node.right.right is None

        return is_terminating or is_continuing_balanced or is_left_nearly_terminating or is_right_nearly_terminating
