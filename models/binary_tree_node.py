from __future__ import annotations

import math


class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.depth = 0
        self.value = value
        self.parent = parent

    def calculate_depths(self) -> int:
        return self._calculate_depths_recursive(self)

    def is_balanced(self) -> bool:
        depth_left = 0 if self.left is None else self.left.depth
        depth_right = 0 if self.right is None else self.right.depth
        return math.fabs(depth_left - depth_right) <= 1

    def next_binary_search_tree_node(self) -> BinaryTreeNode:
        if self.right is not None:
            next_node = self.right
            while next_node.left is not None:
                next_node = next_node.left
        else:
            next_node = self
            while next_node is not None and next_node.value <= self.value:
                next_node = next_node.parent

        return next_node

    def _calculate_depths_recursive(self, node: BinaryTreeNode) -> int:
        max_depth = 0
        if node.left is not None:
            max_depth = self._calculate_depths_recursive(node.left) + 1

        if node.right is not None:
            depth_right = self._calculate_depths_recursive(node.right) + 1
            max_depth = max_depth if max_depth >= depth_right else depth_right

        node.depth = max_depth

        return max_depth

    def __str__(self):
        return str(self.value)
