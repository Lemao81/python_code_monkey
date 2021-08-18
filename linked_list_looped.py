from common import create_linked_list, get_linked_list_last_node
from models.node import Node


def check_is_looped_list1(first_node: Node):
    hash_map = {}
    while first_node.next is not None:
        if first_node.next in hash_map:
            return first_node.next
        else:
            hash_map[first_node.next] = True
            first_node = first_node.next
    return None


def check_is_looped_list2(first_node: Node):
    slow_runner = first_node
    fast_runner = first_node
    while fast_runner is not None and fast_runner.next is not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next
        if fast_runner == slow_runner:
            break
    if fast_runner is None or fast_runner.next is None:
        return None
    slow_runner = first_node
    while fast_runner is not slow_runner:
        fast_runner = fast_runner.next
        slow_runner = slow_runner.next
    return fast_runner


def print_result(loop_node: Node):
    is_looped = loop_node is not None
    print(f'IS looped (id {loop_node.id})' if is_looped else 'Is NOT looped')


if __name__ == '__main__':
    looped_list = create_linked_list(20)
    get_linked_list_last_node(looped_list).next = looped_list.next.next.next.next.next.next.next
    non_looped_list = create_linked_list(20)

    print()
    print_result(check_is_looped_list1(looped_list))
    print_result(check_is_looped_list1(non_looped_list))
    print()

    print_result(check_is_looped_list2(looped_list))
    print_result(check_is_looped_list2(non_looped_list))
    print()
