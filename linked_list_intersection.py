from models.node import Node
from common import create_linked_list


def check_node_intersection1(first: Node, second: Node):
    while first is not None:
        second_runner = second
        while second_runner is not None:
            if first == second_runner:
                return first
            second_runner = second_runner.next
        first = first.next
    return None


def check_node_intersection2(first: Node, second: Node):
    first_hash = {}
    while first is not None:
        first_hash[first] = True
        first = first.next
    while second is not None:
        if second in first_hash:
            return second
        second = second.next
    return None


def check_node_intersection3(first: Node, second: Node):
    (is_intersecting, first_length, second_length) = check_is_intersecting_and_return_lengths(first, second)
    if not is_intersecting:
        return None
    longer_one = first if first_length > second_length else second
    shorter_one = second if first_length > second_length else first
    for i in range(abs(first_length - second_length)):
        longer_one = longer_one.next
    while longer_one is not None and shorter_one is not None:
        if longer_one == shorter_one:
            return longer_one
        longer_one = longer_one.next
        shorter_one = shorter_one.next
    raise Exception


def check_is_intersecting_and_return_lengths(first: Node, second: Node):
    first_length = 1
    while first.next is not None:
        first_length += 1
        first = first.next
    second_length = 1
    while second.next is not None:
        second_length += 1
        second = second.next
    return first == second, first_length, second_length


def get_intersecting_message(node: Node) -> str:
    return 'not intersecting' if node is None else f'intersecting (id {str(node.id)})'


if __name__ == '__main__':
    first_non_intersecting = create_linked_list(10)
    second_non_intersecting = create_linked_list(13)
    first_intersecting = create_linked_list(20)
    second_intersecting = create_linked_list(10)
    intersecting_node = first_intersecting.next.next.next.next.next.next.next.next.next.next.next.next.next
    intersecting_node.next = second_intersecting.next.next.next

    candidate = check_node_intersection1(first_non_intersecting, second_non_intersecting)
    print('Expect non-intersection, and is: ' + get_intersecting_message(candidate))
    print()

    candidate = check_node_intersection1(first_intersecting, second_intersecting)
    print('Expect intersection, and is: ' + get_intersecting_message(candidate))
    print()

    candidate = check_node_intersection2(first_non_intersecting, second_non_intersecting)
    print('Expect non-intersection, and is: ' + get_intersecting_message(candidate))
    print()

    candidate = check_node_intersection2(first_intersecting, second_intersecting)
    print('Expect intersection, and is: ' + get_intersecting_message(candidate))
    print()

    candidate = check_node_intersection3(first_non_intersecting, second_non_intersecting)
    print('Expect non-intersection, and is: ' + get_intersecting_message(candidate))
    print()

    candidate = check_node_intersection3(first_intersecting, second_intersecting)
    print('Expect intersection, and is: ' + get_intersecting_message(candidate))
    print()
