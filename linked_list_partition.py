from common import create_linked_list, print_linked_list, linked_list_insert_after

from models.node import Node


def partition_linked_list(current_node: Node, partition: int):
    if current_node.next is not None:
        (connect_node, last_node) = partition_linked_list(current_node.next, partition)
    else:
        return (current_node, current_node)
    if current_node.value >= partition and current_node.next is not None:
        last_node.next = current_node
        current_node.next = None
        return (connect_node, current_node)
    else:
        current_node.next = connect_node
    return (current_node, last_node)


if __name__ == '__main__':
    node_count = 20

    first_node = create_linked_list(node_count)
    print_linked_list('Initial list 1:', first_node)
    print()

    partition = int(input('Partition value: '))

    (first_node, _) = partition_linked_list(first_node, partition)
    print_linked_list('After partitioning:', first_node)
    print()
