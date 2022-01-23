from models.binary_search_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree.create_random(10, 100)
    tree.print()
    nodes_sorted = tree.get_nodes_sorted()
    nodes_pre_order = tree.root.get_nodes_pre_order()

    print(list(map(lambda x: x.value, nodes_sorted)))
    print(list(map(lambda x: x.value, nodes_pre_order)))
    print(tree.get_random_node().value)

    tree.delete(20)
    tree.print()