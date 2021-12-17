import common

if __name__ == '__main__':
    tree = common.create_random_binary_tree(5)
    # tree.root.right.right = None
    tree.print()
    print()
    print('Is balanced' if tree.is_balanced2() else 'Is NOT balanced')
