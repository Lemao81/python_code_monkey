from common import create_random_binary_tree
from code_challenges import check_is_subtree_of

if __name__ == '__main__':
    tree1 = create_random_binary_tree(13)
    tree1.print()
    tree2 = create_random_binary_tree(1)
    tree2.print()
    is_subtree = check_is_subtree_of(tree1, tree2)
    print('IS subtree' if is_subtree else 'IS NOT subtree')
