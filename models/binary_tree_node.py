from __future__ import annotations

import math


class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 0
        self.parent = parent
        self.node_count = 0

    def calculate_depths(self) -> int:
        return self._calculate_depths_recursive(self)

    def is_balanced_by_depth(self) -> bool:
        depth_left = 0 if self.left is None else self.left.depth
        depth_right = 0 if self.right is None else self.right.depth
        return math.fabs(depth_left - depth_right) <= 1

    def is_balanced(self) -> bool:
        if self is None:
            return True

        is_terminating = self.left is None and self.right is None
        is_continuing_balanced = self.left is not None and self.right is not None
        is_left_nearly_terminating = self.right is None and self.left is not None and self.left.left is None and self.left.right is None
        is_right_nearly_terminating = self.left is None and self.right is not None and self.right.left is None and self.right.right is None
        return is_terminating or is_continuing_balanced or is_left_nearly_terminating or is_right_nearly_terminating

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

    def get_nodes_pre_order(self) -> [BinaryTreeNode]:
        def collect_pre_order_recursive(collected_nodes: [BinaryTreeNode], node: BinaryTreeNode):
            if node is None:
                return
            collected_nodes.append(node)
            collect_pre_order_recursive(collected_nodes, node.left)
            collect_pre_order_recursive(collected_nodes, node.right)

        nodes = []
        collect_pre_order_recursive(nodes, self)
        return nodes

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
