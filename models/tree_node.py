import math


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print(self):
        levels = [[]]
        self._print_traverse(0, levels, self)
        levels = list(filter(lambda x: any(map(lambda y: y != '--', x)), levels))
        level_count = len(levels)
        max_value_count = int(math.pow(2, level_count - 1))
        value_gap_count = 2
        branch_gap_count = 4
        max_width = math.floor(max_value_count / 2) * value_gap_count + (math.floor(max_value_count / 2) - 1) * branch_gap_count
        for i, level in enumerate(levels):
            to_print = []
            for j, c in enumerate(level):
                to_print.append(c)
                to_print.append(' ' * value_gap_count if j % 2 == 0 else ' ' * branch_gap_count)
            print(''.join(to_print).center(max_width))

    def _print_traverse(self, level_index: int, levels: [[int]], node):
        if len(levels) == level_index:
            levels.append([])
        if node is not None:
            levels[level_index].append(str(node.value).rjust(2, ' '))
            self._print_traverse(level_index + 1, levels, node.left)
            self._print_traverse(level_index + 1, levels, node.right)
        else:
            levels[level_index].append('--')
