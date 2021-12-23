import common

if __name__ == '__main__':
    tree = common.create_binary_search_tree([2, 5, 23, 13, 53, 17, 67, 98, 42, 84, 22, 13, 82, 48, 94, 12])
    tree.print()
    print()
    print(tree.root.left.left.right.next_binary_search_tree_node().value)
