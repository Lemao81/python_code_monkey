import common

if __name__ == '__main__':
    tree = common.create_binary_search_tree([2, 5, 23, 13, 53, 17, 67, 98])
    tree.print()
    print()
    print('Is search tree' if tree.is_search_tree2() else 'Is NOT search tree')
