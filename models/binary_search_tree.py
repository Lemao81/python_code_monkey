from models.binary_tree import BinaryTree
from models.binary_tree_node import BinaryTreeNode
import random


class BinarySearchTree(BinaryTree):
    def __init__(self, root_value):
        super().__init__(root_value)

    @staticmethod
    def create_random(node_count, max_value):
        tree = BinarySearchTree(random.randint(1, max_value))
        for i in range(node_count):
            tree.insert(random.randint(1, max_value))
        return tree

    def insert(self, value):
        new_node = BinaryTreeNode(value)
        self._insert_recursive(self.root, new_node)

    def find(self, value) -> BinaryTreeNode | None:
        return self._find_recursive(self.root, value)

    def delete(self, value):
        def find_parent_recursive(node: BinaryTreeNode) -> BinaryTreeNode | None:
            if node is None:
                return None
            if node.left is not None and node.left.value == value or node.right is not None and node.right.value == value:
                return node
            return find_parent_recursive(node.left) if value < node.value else find_parent_recursive(node.right)

        parent_of_delete = find_parent_recursive(self.root)
        if parent_of_delete is None:
            return
        is_left_delete = parent_of_delete.left is not None and parent_of_delete.left.value == value
        node_to_delete = parent_of_delete.left if is_left_delete else parent_of_delete.right
        child_nodes = node_to_delete.get_nodes_pre_order()
        child_nodes.remove(node_to_delete)
        if is_left_delete:
            parent_of_delete.left = None
        else:
            parent_of_delete.right = None
        for child in child_nodes:
            child.left = child.right = None
            self.insert(child)

    def get_nodes_sorted(self) -> [BinaryTreeNode]:
        nodes = []
        self.traverse_in_order(lambda x: nodes.append(x))
        return nodes

    def get_random_node(self):
        nodes = self.get_nodes_sorted()
        return nodes[random.randint(0, len(nodes) - 1)]

    def _insert_recursive(self, compare_node: BinaryTreeNode, new_node: BinaryTreeNode):
        if new_node.value <= compare_node.value:
            if compare_node.left is None:
                compare_node.left = new_node
                new_node.parent = compare_node
            else:
                self._insert_recursive(compare_node.left, new_node)
        else:
            if compare_node.right is None:
                compare_node.right = new_node
                new_node.parent = compare_node
            else:
                self._insert_recursive(compare_node.right, new_node)
        compare_node.node_count += 1

    def _find_recursive(self, candidate: BinaryTreeNode, value) -> BinaryTreeNode | None:
        if candidate is None:
            return None
        if candidate.value == value:
            return candidate
        if value < candidate.value:
            self._find_recursive(candidate.left, value)
        else:
            self._find_recursive(candidate.right, value)
