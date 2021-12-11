from common import create_linked_list, print_linked_list
from models.linked_list_node import LinkedListNode


def linked_list_skip(first_node: LinkedListNode, skip_count: int):
    while first_node is not None and skip_count > 0:
        first_node = first_node.next
        skip_count -= 1
    return first_node


def linked_list_skip2(first_node: LinkedListNode, skip_count: int):
    for i in range(skip_count):
        first_node = first_node.next
        if first_node is None:
            return None
    return first_node


def count_linked_list(first_node: LinkedListNode):
    counter = 0
    while first_node is not None:
        first_node = first_node.next
        counter += 1
    return counter


def iterate_linked_list(first_node: LinkedListNode, count: int, k: int):
    if first_node.next is None:
        return count, first_node, count == k
    else:
        (size, node, reached) = iterate_linked_list(first_node.next, count + 1, k)
        if size - count + 1 == k:
            return size, first_node, True
        if reached:
            return size, node, True
        return size, None, False


def iterate_linked_list2(first_node: LinkedListNode, count: int, k: int):
    if first_node.next is None:
        return 1, first_node
    else:
        (reverse_count, node) = iterate_linked_list2(first_node.next, count + 1, k)
        if reverse_count == k - 1:
            return reverse_count + 1, first_node
        return reverse_count + 1, node


def iterate_linked_list3(first_node: LinkedListNode, k: int):
    runner = first_node
    runner_count = 0
    while runner is not None:
        runner_count += 1
        runner = runner.next
        if runner_count > k:
            first_node = first_node.next
    return first_node


if __name__ == '__main__':
    k = int(input('kth: '))
    node_count = 10
    first_node = create_linked_list(node_count)
    print_linked_list('Initial list 1:', first_node)
    print()

    print_linked_list(f'{k}th to last element:', linked_list_skip2(first_node, count_linked_list(first_node) - k))
    print()

    first_node = create_linked_list(node_count)
    print_linked_list('Initial list 2:', first_node)
    print()

    print_linked_list(f'{k}th to last element, recursive call:', iterate_linked_list2(first_node, 0, k)[1])
    print()

    first_node = create_linked_list(node_count)
    print_linked_list('Initial list 3:', first_node)
    print()

    print_linked_list(f'{k}th to last element, iterative call with runner:', iterate_linked_list3(first_node, k))
