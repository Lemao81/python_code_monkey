from common import create_linked_list, print_linked_list
from models.linked_list_node import LinkedListNode

node_id = 0


def sort_linked_list(first_node: LinkedListNode):
    current_node = first_node
    prev_current_node = None
    while current_node is not None:
        prev_compare_node = current_node
        compare_node = current_node.next
        while compare_node is not None:
            if compare_node.value < current_node.value:
                swap_nodes(prev_current_node, current_node, prev_compare_node)
                if current_node is first_node:
                    first_node = compare_node
                temp = current_node
                current_node = compare_node
                compare_node = temp
            else:
                prev_compare_node = compare_node
            compare_node = compare_node.next
        prev_current_node = current_node
        current_node = current_node.next
    return first_node


def swap_nodes(before_left_node, left_node: LinkedListNode, before_right_node: LinkedListNode):
    right_node = before_right_node.next
    if before_left_node is not None:
        before_left_node.next = right_node
    before_right_node.next = left_node
    temp = left_node.next
    left_node.next = right_node.next
    right_node.next = temp


def remove_duplicates_from_unsorted(first_node):
    values = []
    current_node = first_node
    prev_node = None
    while current_node is not None:
        if current_node.value in values:
            prev_node.next = current_node.next
        else:
            values.append(current_node.value)
            prev_node = current_node
        current_node = current_node.next


def remove_duplicates_from_unsorted2(first_node):
    current_node = first_node
    while current_node.next is not None:
        compare_node = current_node
        while compare_node.next is not None:
            if compare_node.next.value == current_node.value:
                compare_node.next = compare_node.next.next
            compare_node = compare_node.next
        current_node = current_node.next
    return first_node


def remove_duplicates_from_sorted(first_node):
    current_node = first_node
    prev_node = None
    while current_node is not None:
        if prev_node is not None and prev_node.value == current_node.value:
            prev_node.next = current_node.next
        else:
            prev_node = current_node
        current_node = current_node.next


if __name__ == '__main__':
    node_count = 20
    first_node = create_linked_list(node_count)
    print_linked_list('With duplicates unsorted:', first_node)
    print()

    remove_duplicates_from_unsorted2(first_node)
    print_linked_list('Duplicates removed unsorted:', first_node)
    print()

    first_node = create_linked_list(node_count)
    print_linked_list('With duplicates unsorted:', first_node)
    print()

    first_node = sort_linked_list(first_node)
    print_linked_list('With duplicates sorted (not working yet):', first_node)
    print()

    remove_duplicates_from_sorted(first_node)
    print_linked_list('Duplicates removed sorted:', first_node)
    print()
