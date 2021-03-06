import math
import sys

from models.binary_tree_node import BinaryTreeNode
from typing import Callable
from typing import List

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

    def find_first_post_order(self, predicate: Callable[[BinaryTreeNode], bool]) -> BinaryTreeNode:
        return self._find_first_post_order_recursive(self.root, predicate)

    def find_all_in_order(self, predicate: Callable[[BinaryTreeNode], bool]) -> [BinaryTreeNode]:
        found = []
        self._find_all_in_order_recursive(self.root, predicate, found)
        return found

    def get_depth(self) -> int:
        return self._get_depth_recursive(self.root, 0)

    def get_depth2(self) -> int:
        self.root.calculate_depths()
        return self.root.depth

    def is_balanced(self) -> bool:
        return self.check_pre_order(BinaryTreeNode.is_balanced)

    def is_balanced2(self) -> bool:
        self.root.calculate_depths()
        return self.check_pre_order(lambda node: node is None or node.is_balanced_by_depth())

    def is_search_tree(self) -> bool:
        values_sorted = self._get_values_sorted_recursive(self.root)
        print(values_sorted)
        current_max = 0
        for i in values_sorted:
            if i < current_max:
                return False
            current_max = i
        return True

    def is_search_tree2(self) -> bool:
        return self._check_search_tree_range(self.root, -sys.maxsize, sys.maxsize)

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

    def _find_first_post_order_recursive(self, node: BinaryTreeNode, predicate: Callable[[BinaryTreeNode], bool]) -> BinaryTreeNode:
        found = None if node is None else self._find_first_post_order_recursive(node.left, predicate)
        if found is not None:
            return found
        found = None if node is None else self._find_first_post_order_recursive(node.right, predicate)
        if found is not None:
            return found
        return node if predicate(node) else None

    def _find_all_in_order_recursive(self, node: BinaryTreeNode, predicate: Callable[[BinaryTreeNode], bool], found: List) -> [BinaryTreeNode]:
        if node is None:
            return
        if predicate(node):
            found.append(node)
        self._find_all_in_order_recursive(node.left, predicate, found)
        self._find_all_in_order_recursive(node.right, predicate, found)

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

    def _get_values_sorted_recursive(self, node: BinaryTreeNode) -> []:
        if node is None:
            return []

        left_values = self._get_values_sorted_recursive(node.left)
        right_values = self._get_values_sorted_recursive(node.right)

        return [*left_values, node.value, *right_values]

    def _check_search_tree_range(self, node: BinaryTreeNode, left_bound: int, right_bound: int) -> bool:
        if node is None:
            return True

        if not left_bound <= node.value <= right_bound:
            return False
        if not self._check_search_tree_range(node.left, left_bound, node.value):
            return False
        if not self._check_search_tree_range(node.right, node.value, right_bound):
            return False
        return True

    @staticmethod
    def _map_depth_level_linked_list_to_print_line(linked_list: LinkedList, total_length: int) -> str:
        result = ''
        count = linked_list.get_count()
        head = linked_list.root
        while head is not None:
            result += str(head.value.value).rjust(2, ' ').center(math.floor(total_length / count), ' ')
            head = head.next
        return result
